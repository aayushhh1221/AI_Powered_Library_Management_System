from App.prompts.intent_prompt import intent_prompt
from App.parsers.intent_parser import intent_parser
from App.utils.llm import llm

intent_chain = (
    intent_prompt
    | llm
    | intent_parser
)