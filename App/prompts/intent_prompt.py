from langchain_core.prompts import ChatPromptTemplate
from App.parsers.intent_parser import intent_parser

intent_prompt = ChatPromptTemplate.from_messages(
[
(
"system",
"""
You are an intent classifier.

Classify the user's request into exactly ONE of these intents:

- recommendation
- summary
- similar
- roadmap
- chat

Return ONLY valid JSON.

{format_instructions}
"""
),
(
"human",
"{question}"
)
]
).partial(
format_instructions=intent_parser.get_format_instructions()
)