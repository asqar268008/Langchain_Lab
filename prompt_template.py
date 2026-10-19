import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model = "llama3",
    model_provider = "ollama"
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {role}"),
    ("human", "{question}")
])

result = prompt_template.invoke(
    {
        "role": "AI Engineer",
        "question": "What is the difference between RAG and Fine-tuning?"
    }
)

response = model.invoke(result)

print("Response:", response.content)