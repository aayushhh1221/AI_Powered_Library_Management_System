from langchain_core.prompts import ChatPromptTemplate
from App.parsers.similar_book_parser import similar_book_parse


similar_books_prompt=ChatPromptTemplate.from_messages(
    [
        ("system","""You are an AI Librarian.

Recommend exactly 3 books similar to the user's book.

For each recommendation provide:
- title
- author
- reason

IMPORTANT:
- Return ONLY raw JSON.
- Do NOT wrap the JSON inside ```json or ``` code blocks.
- Do NOT include markdown.
- Do NOT include explanations.
- Do NOT write any text before or after the JSON.

{format_instructions}

{format_instructions}"""),("human",
                           "{question}")
    ]
).partial(format_instructions=similar_book_parse.get_format_instructions())