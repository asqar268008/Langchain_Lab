import os
import urllib
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.postgres import PostgresSaver
from dotenv import load_dotenv

load_dotenv()

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
encoded_password = urllib.parse.quote_plus(POSTGRES_PASSWORD)

DB = f"postgresql://postgres:{encoded_password}@localhost:5432/chat_history"


with PostgresSaver.from_conn_string(DB) as checkpointer:
    checkpointer.setup()

    model = init_chat_model(
        model = "llama3",
        model_provider = "ollama",
        #api_key = os.getenv("API_KEY")
    )

    agent = create_agent(
        model = model,
        checkpointer = checkpointer
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