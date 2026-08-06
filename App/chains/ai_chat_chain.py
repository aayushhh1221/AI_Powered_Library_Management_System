from langchain_core.runnables import RunnablePassthrough
from App.chains.intent_chain import intent_chain
from langchain_core.runnables import RunnableBranch
from App.chains.recommendation_chain import chat_chain
from App.chains.roadmap_chain import chain
from App.chains.similar_book_chain import similar_chain
from App.chains.summary_chain import summary_chain


router_input = RunnablePassthrough.assign(
    intent=lambda x: intent_chain.invoke(
        {
            "question": x["question"]
        }
    ).intent
)



branch = RunnableBranch(

(
lambda x: x["intent"]=="recommendation",

chat_chain
),

(
lambda x: x["intent"]=="summary",

summary_chain
),

(
lambda x: x["intent"]=="similar",

similar_chain
),

(
lambda x: x["intent"]=="roadmap",

chain
),

chat_chain

)

ai_router_chain = (
    router_input
    | branch
)