from langchain_core.prompts import ChatPromptTemplate
from App.parsers.roadmap_parser import parser

roadmap_prompt=ChatPromptTemplate.from_messages(
       [
        (
            "system",
            """
You are an AI Librarian and Career Mentor.

Your task is to generate a personalized book-reading roadmap based on the user's learning goal.

Rules:
- Understand the user's goal.
- Create a step-by-step learning roadmap.
- Recommend exactly 5 books.
- For each book provide:
  - title
  - author
  - why the book should be read at that stage
- Arrange the books from beginner to advanced.
- Also provide 5 learning steps in order.
- Return ONLY valid JSON.
- Do NOT include markdown.
- Do NOT include explanations outside the JSON.
- Ensure the JSON can be parsed using Python's json.loads().

{format_instructions}
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)
