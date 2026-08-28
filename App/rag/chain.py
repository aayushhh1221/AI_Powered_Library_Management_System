from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from App.rag.vector_store import get_retriever
from App.utils.llm import llm


rag_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an AI librarian.

Answer the user's question using ONLY the provided context.

If the answer is not present in the context, say:
"I couldn't find this information in the book."

Do not make up information.

Context:
{context}
"""
    ),
    (
        "human",
        "{question}"
    )
])


def get_rag_chain(book_id: str):

    retriever = get_retriever(book_id)

    def format_docs(docs):
        return "\n\n".join(
            doc.page_content for doc in docs
        )

    chain = (
        {
            "context": retriever | format_docs,
            "question": lambda x: x
        }
        | rag_prompt
        | llm
        | StrOutputParser()
    )

    return chain