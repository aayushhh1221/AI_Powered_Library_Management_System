from langchain_google_genai import ChatGoogleGenerativeAI
from App.config.settings import settings

llm=ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=settings.GEMINI_API_KEY,
)

