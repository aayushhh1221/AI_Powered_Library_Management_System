from langchain_core.output_parsers import PydanticOutputParser
from App.parsers.ai_schems import Roadmap

parser=PydanticOutputParser(
    pydantic_object=Roadmap
)