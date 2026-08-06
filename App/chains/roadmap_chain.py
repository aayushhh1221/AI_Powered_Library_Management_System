from App.utils.llm import llm
from App.prompts.roadmap import roadmap_prompt
from App.parsers.roadmap_parser import parser

chain=roadmap_prompt|llm|parser