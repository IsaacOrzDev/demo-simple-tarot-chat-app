from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from chromadb.utils import embedding_functions
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

loader = TextLoader('./src/data/cards.txt')
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)


embedding_functions = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2")

vector_db = Chroma.from_documents(
    texts, embedding_functions, persist_directory="db")

vector_db.persist()
