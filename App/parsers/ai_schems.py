from pydantic import BaseModel

class Book(BaseModel):
    title:str
    author:str
    reason:str

class BookRecommendation(BaseModel):
    books:list[Book]

class ChatRequest(BaseModel):
    question:str

class summary_book(BaseModel):
    question:str

class SimilarBookRecommendation(BaseModel):
    question:list[Book]

class Roadmap(BaseModel):
    books:list[Book]
    question:str

class RoadmapRequest(BaseModel):
    question:str

class Intent(BaseModel):
    intent:str

class RAGRequest(BaseModel):
    book_id: str
    question: str