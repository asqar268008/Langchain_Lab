import os
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model = "gemini-3.8-flash",
    model_provider = "google-genai",
    api_key = os.getenv("API_KEY")
)

agent = create_agent(
    model = model,
    checkpointer = InMemorySaver()
)

while True:
    input_text = input("You: ")
    if input_text.lower() == "exit":
        break
    response = agent.invoke({
        "messages": [
            {"role": "user", "content": input_text}
        ]
    }, config = {
        "configurable": {
        "thread_id": 1002
        }
    })

    print("Response:", response["messages"][-1].content)