from langchain_core.output_parsers import PydanticOutputParser
from App.parsers.ai_schems import BookRecommendation

recommendation_parser=PydanticOutputParser(
    pydantic_object=BookRecommendation
)