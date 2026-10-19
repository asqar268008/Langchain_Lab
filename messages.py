import os
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model = "gemini-3.8-flash",
    model_provider = "google-genai",
    api_key = os.getenv("API_KEY")
)

conversation = [
    SystemMessage(content =
                  """You are a helpful assistant, 
                  You will answer only Math questions."""),
    HumanMessage(content = "What is the integral of x^2?"),
    AIMessage(content = "The integral of x^2 is (1/3)x^3 + C, where C is the constant of integration."),
    HumanMessage(content = "What is java?")
]

response = model.invoke(conversation)
print("Response:", response.content)