import os
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model = "gemini-3.8-flash",
    model_provider = "google_genai",
    api_key = os.getenv("API_KEY")
)

@tool
def send_money(amount: float, person: str) -> str:
    "Send money to a person and return a confirmation message."
    confirm = input(f"Do you want to send ${amount} to {person}? (yes/no): ")
    if (confirm.lower() == "yes"):
        return f"Sent ${amount} to {person}."
    else:
        return "Transaction cancelled."

agent = create_agent(
    model = model,
    tools = [send_money]
)

response = agent.invoke({
    "messages": [
        {"role": "user", "content": "Send $100 to John."}
    ]
})

print(response["messages"][-1].content)