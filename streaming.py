import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model = "gemini-3.8-flash",
    model_provider = "google-genai",
    api_key = os.getenv("API_KEY")
)

for chunk in model.stream("What is the difference between RAG and Fine-tuning?"):
    print(chunk.content, end="", flush = True)