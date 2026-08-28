from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vectorstore = Chroma(
    collection_name="library_books",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)


def add_documents(documents):
    vectorstore.add_documents(documents)


def get_retriever(book_id: str):
    return vectorstore.as_retriever(
        search_kwargs={
            "k": 4,
            "filter": {"book_id": book_id}
        }
    )