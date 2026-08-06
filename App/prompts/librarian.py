from langchain_core.prompts import ChatPromptTemplate
from App.parsers.recommendation_parser import recommendation_parser

LIBRARIAN_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Librarian.

Your job is to recommend books based on the user's interests.

Rules:
- Recommend exactly THREE books.
- Include the title, author, and a short reason.
- Return ONLY valid JSON.
- Do not include markdown.
- Do not include explanations outside the JSON.

{format_instructions}
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
).partial(
    format_instructions=recommendation_parser.get_format_instructions()
)