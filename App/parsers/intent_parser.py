from langchain_core.output_parsers import PydanticOutputParser
from App.parsers.ai_schems import Intent

intent_parser = PydanticOutputParser(
    pydantic_object=Intent
)