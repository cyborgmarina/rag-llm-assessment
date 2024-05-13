from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_weaviate.vectorstores import WeaviateVectorStore

from typing import List
from fastapi import HTTPException, status
from app.models import Document

import weaviate
from weaviate.connect import ConnectionParams
from weaviate.classes.init import AdditionalConfig, Timeout

class DocumentService:
    def __init__(self):
        self.documents = set()
        self.weaviate_client = self._connect_to_weaviate()

    def _connect_to_weaviate(self) -> weaviate.Client:
        client = weaviate.WeaviateClient(
            connection_params=ConnectionParams.from_params(
                http_host="vectordb",
                http_port="8080",
                http_secure=False,
                grpc_host="vectordb",
                grpc_port="50051",
                grpc_secure=False,
            ),
            additional_config=AdditionalConfig(
                timeout=Timeout(init=2, query=45, insert=120),  # Values in seconds
            ),
        )
        client.connect()
        return client


    def add_document(self, document: Document):
        if document.text in self.documents:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Duplicate text detected")
        self.documents.add(document.text)

        # Split text into chunks
        docs = self._split_text([document.text])

        # Create embeddings and store in Weaviate
        self._store_in_weaviate(docs)


    def _split_text(self, texts: List[str]) -> List[str]:
        text_splitter = CharacterTextSplitter(
            separator="",
            chunk_size=1000,
            chunk_overlap=0,
            length_function=len,
            is_separator_regex=False
        )
        return text_splitter.create_documents(texts)

    def _store_in_weaviate(self, docs: List[str]):
        embeddings = SpacyEmbeddings(model_name="pt_core_news_sm")
        db = WeaviateVectorStore.from_documents(docs, embeddings, client=self.weaviate_client)

