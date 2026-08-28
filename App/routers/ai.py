from fastapi import APIRouter,UploadFile, File, Form,Request,Depends
import os
import uuid
from App.parsers.ai_schems import ChatRequest,summary_book,RoadmapRequest,RAGRequest
from App.services.chain import recommend_book,summary,get_similar_book,roadmap,chat
from App.rag.ingest import ingest_book
from App.rag.chain import get_rag_chain
from App.core.limiter import limiter
from App.security import get_current_user
from App.models import User

router=APIRouter(prefix="/ai",tags=["AI"])

@router.post("/recommend")
@limiter.limit("5/minute")
def chat_with_ai(request:Request,data:ChatRequest,current_user: User = Depends(get_current_user)):
    return recommend_book(data.question)

@router.post("/summary")
@limiter.limit("5/minute")
def generate_summary(request:Request,data:summary_book,current_user: User = Depends(get_current_user)):
    return summary(data.question)

@router.post("/similarbooks")
@limiter.limit("5/minute")
def search_similar(request:Request,data:summary_book,current_user: User = Depends(get_current_user)):
    return get_similar_book(data.question)

@router.post("/roadmap")
@limiter.limit("5/minute")
def get_roadmap(request:Request,data:RoadmapRequest,current_user: User = Depends(get_current_user)):
    return roadmap(data.question)


@router.post("/chat")
@limiter.limit("10/minute")
def chat_endpoint(request: Request,data: ChatRequest,current_user: User = Depends(get_current_user)):

    return chat(data.question)


@router.post("/upload-book")
@limiter.limit("3/minute")
async def upload_book(request: Request,
    file: UploadFile = File(...),
    book_name: str = Form(...),current_user: User = Depends(get_current_user)
):

    if file.content_type != "application/pdf":
        return {
            "error": "Only PDF files are allowed"
        }

    book_id = str(uuid.uuid4())

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{book_id}.pdf"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    result = ingest_book(
        file_path=file_path,
        book_id=book_id,
        book_name=book_name
    )

    return {
        "message": "Book uploaded successfully",
        **result
    }

@router.post("/rag")
@limiter.limit("5/minute")
def rag_chat(request:Request,data: RAGRequest,current_user: User = Depends(get_current_user)):

    chain = get_rag_chain(data.book_id)

    answer = chain.invoke(data.question)

    return {
        "book_id": data.book_id,
        "question": data.question,
        "answer": answer
    }


