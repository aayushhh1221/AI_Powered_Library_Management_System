from langchain_core.output_parsers import PydanticOutputParser
from App.parsers.ai_schems import SimilarBookRecommendation

similar_book_parse=PydanticOutputParser(
    pydantic_object=SimilarBookRecommendation
)

