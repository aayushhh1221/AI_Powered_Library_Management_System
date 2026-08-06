from App.chains.recommendation_chain import chat_chain
from App.chains.summary_chain import summary_chain
from App.chains.similar_book_chain import similar_chain
from App.chains.roadmap_chain import chain
from App.chains.ai_chat_chain import ai_router_chain

def recommend_book(question:str):
    response=chat_chain.invoke({
        "question":question
    })
    return response

def summary(question:str):
    final_summary=summary_chain.invoke({
        "question":question
    })
    return final_summary

def get_similar_book(question:str):
    response=similar_chain.invoke({
        "question":question
    })
    return response

def roadmap(question:str):
    response=chain.invoke(
        {
            "question":question
        }
    )
    return response

def chat(question: str):

    return ai_router_chain.invoke(
        {
            "question": question
        }
    )