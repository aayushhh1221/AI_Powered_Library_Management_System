from App.rag.loader import load_pdf
from App.rag.splitter import split_documents
from App.rag.vector_store import add_documents


def ingest_book(file_path: str, book_id: str, book_name: str):

    documents = load_pdf(file_path)

    chunks = split_documents(documents)

    for chunk in chunks:
        chunk.metadata["book_id"] = book_id
        chunk.metadata["book_name"] = book_name

    add_documents(chunks)

    return {
        "book_id": book_id,
        "book_name": book_name,
        "pages": len(documents),
        "chunks": len(chunks)
    }