
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model = "gemini-3.8-flash",
    model_provider = "google-genai",
    api_key = os.getenv("API_KEY")
)

while True:
    input_text = input("You: ")
    if input_text.lower() == "exit":
        break
    response = model.invoke(input_text)
    print("Response:", response.content[0][1])