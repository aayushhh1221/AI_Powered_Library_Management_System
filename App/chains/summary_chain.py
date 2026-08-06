from App.utils.llm import llm
from App.prompts.summary import summary_prompt
from App.parsers.summary_parser import parser

summary_chain=summary_prompt|llm|parser
