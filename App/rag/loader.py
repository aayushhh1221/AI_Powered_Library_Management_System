from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

load_dotenv()

def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    return loader.load()