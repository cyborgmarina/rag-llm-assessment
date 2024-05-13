import weaviate

from bs4 import BeautifulSoup
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_weaviate.vectorstores import WeaviateVectorStore


sample_hotmart_long_text = """
Afinal, como funciona a Hotmart? Quem começa a se aprofundar nas alternativas que o marketing digital oferece no empreendedorismo vai ouvir falar na Hotmart.

E aqui a gente te explica o que é, como funciona e como você pode trabalhar com a plataforma.

Você sabia que a Hotmart é uma empresa global de tecnologia que oferece uma plataforma para venda de conteúdos digitais completa e com a melhor estrutura para criadores de conteúdo, Produtores, Afiliados, compradores e é líder de mercado em toda a América Latina?

Mas, para muito além de uma plataforma digital, somos uma empresa cuja missão é fazer o que for possível para que você viva das suas paixões. Seja criando um negócio digital e aumentando sua renda ou fazendo um curso online para aprender novas habilidades.

E como fazemos isso? Juntando as três pontas do processo de venda online: Produtor, Afiliado e Comprador!

Parece complicado, mas, na verdade, é muito simples. 

Se você quer trabalhar com vendas na internet ou fazer um curso online para expandir suas possibilidades, continue sua leitura para entender detalhadamente como a Hotmart funciona e por que ela é a sua escolha certa!

Veja só o que você vai aprender neste post:
"""

urls = ["https://hotmart.com/pt-br/blog/como-funciona-hotmart"]
loader = AsyncHtmlLoader(urls)
print(loader)
docs = loader.load()
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=0,
    length_function=len,
    is_separator_regex=False,
)

metadatas = []
texts = []
for doc in docs:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(doc.page_content, 'html.parser')
    # Extract text from the parsed HTML
    text = soup.get_text(separator='\n', strip=True)
    
    texts.append(text)
    

docs = text_splitter.create_documents(texts)
print(f"Docs: {docs}")
embeddings = SpacyEmbeddings(model_name="pt_core_news_sm")
weaviate_client = weaviate.connect_to_local()
db = WeaviateVectorStore.from_documents(docs, embeddings, client=weaviate_client)
print("####")
print("####")
print("####")
print("####")
print("####")
print("####")
query = "como aumento minhas vendas com a hotmart?"
print(f"query: {query}")
docs = db.similarity_search(query)
print(f"Found {len(docs)} similar docs")

for doc in docs:
    print(doc)


