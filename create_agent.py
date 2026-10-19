import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain.agents import create_agent

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
    print(f"Fetching weather for {city}...")
    return f"The current weather in {city} is sunny with a temperature of 25°C."

@tool
def Gold_rate(country: str) -> str:
    """
    Get the current gold rate for a given amount in rupees.
    """
    print(f"Fetching gold rate for {country}...")
    return f"The current gold rate in {country} is 13,789 rupees per gram."

agent = create_agent(
    model = model,
    tools = [Weather, Gold_rate]
)

response = agent.invoke({
    "messages": [
        {"role": "user", 
        "content": "What is the current Gold Rate in New York?"}
    ]
})

print("Response:", response["messages"][-1].content)