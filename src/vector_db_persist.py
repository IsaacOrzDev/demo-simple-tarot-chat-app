from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from chromadb.utils import embedding_functions
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import os

path = './src/data'
all_texts = []

for filename in os.listdir(path):
    file_path = f"{path}/{filename}"
    print(file_path)
    loader = TextLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    all_texts = all_texts + texts

embedding_functions = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2")

vector_db = Chroma.from_documents(
    all_texts, embedding_functions, persist_directory="db")

vector_db.persist()
