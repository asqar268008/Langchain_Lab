import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class MathQuestion(BaseModel):
    num1: int
    num2: int
    operation: str
    result: int

model = init_chat_model(
    model = "gemini-3.8-flash",
    model_provider = "google-genai",
    api_key = os.getenv("API_KEY")
)

result = model.with_structured_output(MathQuestion)

response = result.invoke(
    "What is the sum of 5 and 3?"
)

print("Response:", response)