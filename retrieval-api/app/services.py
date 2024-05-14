from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams
from weaviate.classes.init import AdditionalConfig, Timeout

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_weaviate.vectorstores import WeaviateVectorStore
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from app.models import Response, Query

from app.constants import (
    OPENROUTER_API_BASE,
    OPENROUTER_API_KEY,
    OPENROUTER_DEFAULT_CHAT_MODEL,
    PROMPT_TEMPLATE,
)


class VectorDatabaseService:
    def __init__(self):
        self.weaviate_client = self._connect_to_weaviate()

    def _connect_to_weaviate(self) -> WeaviateClient:
        client = WeaviateClient(
            connection_params=ConnectionParams.from_params(
                http_host="vectordb",
                http_port=8080,
                http_secure=False,
                grpc_host="vectordb",
                grpc_port=50051,
                grpc_secure=False,
            ),
            additional_config=AdditionalConfig(
                timeout=Timeout(init=2, query=45, insert=120),  # Values in seconds
            ),
        )
        client.connect()
        return client


class AugmentedRetrievalService:
    def __init__(self):
        embedding = SpacyEmbeddings(model_name="pt_core_news_sm")
        client = VectorDatabaseService().weaviate_client
        vectorStore = WeaviateVectorStore(
            client=client,
            text_key="text",
            index_name="knowledgebase",
            embedding=embedding,
        )
        self.retriever = vectorStore.as_retriever()
        self.generated_responses = []

    def _format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def get_generated_responses(self):
        return self.generated_responses

    def generate_response_from_knowledge_base(self, question: str) -> Response:
        llm = ChatOpenAI(
            base_url=OPENROUTER_API_BASE,
            api_key=OPENROUTER_API_KEY,
            model=OPENROUTER_DEFAULT_CHAT_MODEL,
            temperature=0.1,
        )
        prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
        rag_chain_from_docs = (
            RunnablePassthrough.assign(context=(lambda x: x["context"]))
            | prompt
            | llm
            | StrOutputParser()
        )

        rag_chain_with_source = RunnableParallel(
            {
                "context": self.retriever | self._format_docs,
                "question": RunnablePassthrough(),
            }
        ).assign(answer=rag_chain_from_docs)

        rag_chain_response = rag_chain_with_source.invoke(question)

        response = Response(
            context=rag_chain_response["context"],
            assistantResponse=rag_chain_response["answer"],
        )

        self.generated_responses.append(response)
        return response
