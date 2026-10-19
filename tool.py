import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool

load_dotenv()

model = init_chat_model(
    model = "gemini-3.8-flash",
    model_provider = "google-genai",
    api_key = os.getenv("API_KEY")
)

@tool
def Weather(city: str) -> str:
    """
    Get the current weather for a given city.
    """
    return f"The current weather in {city} is sunny with a temperature of 25°C."

@tool
def Gold_rate(country: str) -> str:
    """
    Get the current gold rate for a given amount in rupees.
    """
    return f"The current gold rate in {country} is 13,789 rupees per gram."

model_with_tools = model.bind_tools([Weather, Gold_rate])

response = model_with_tools.invoke(
    "What is the current Gold Rate in New York?"
)

print("Response:", response.tool_calls)