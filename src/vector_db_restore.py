from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

embedding_functions = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2")

vector_db = Chroma(persist_directory="db",
                   embedding_function=embedding_functions)