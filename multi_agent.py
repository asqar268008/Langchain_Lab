import os

from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model = "llama3",
    model_provider = "ollama",
    #api_key = os.getenv("API_KEY")
)

@tool
def addition(num1: int, num2: int) -> int:
    """
    Add two numbers and return the result.
    """
    print("Call Addition Tool")
    return num1 + num2

@tool
def subtraction(num1: int, num2: int) -> int:
    """
    Subtract two numbers and return the result.
    """
    print("Call Subtraction Tool")
    return num1 - num2

@tool
def multiplication(num1: int, num2: int) -> int:
    """
    Multiply two numbers and return the result.
    """
    print("Call Multiplication Tool")
    return num1 * num2

@tool
def division(num1: int, num2: int) -> float:
    """
    Divide two numbers and return the result.
    """
    print("Call Division Tool")
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

agent = create_agent(
    model = model,
    tools = [addition, subtraction, multiplication, division]
)

response = agent.invoke({
    "messages": [
        {"role": "user", "content": "What is 30 times 0 and what is 20 add 10?"}
    ]
})

print("Response:", response["messages"][-1].content)