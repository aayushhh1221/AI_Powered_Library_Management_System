from fastapi import APIRouter
from App.parsers.ai_schems import ChatRequest,summary_book,RoadmapRequest
from App.services.chain import recommend_book,summary,get_similar_book,roadmap,chat
router=APIRouter(tags=["AI"])

@router.post("/recommend")
def chat_with_ai(request:ChatRequest):
    return recommend_book(request.question)

@router.post("/summary")
def generate_summary(request:summary_book):
    return summary(request.question)

@router.post("/similarbooks")
def search_similar(request:summary_book):
    return get_similar_book(request.question)

@router.post("/roadmap")
def get_roadmap(request:RoadmapRequest):
    return roadmap(request.question)


@router.post("/chat")
def chat_endpoint(request: ChatRequest):

    return chat(request.question)