# from langchain.chat_models import ChatOpenAI
import os

from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from tools import fetch_order_status, recommend_products

def create_agent()  :
    print("Creating agent...")
    print("OpenAI API Key : "+ os.getenv("OPENAI_API_KEY"))
    model_name = os.getenv("OPENAI_MODEL", "gpt-4o")
    llm = ChatOpenAI(model=model_name, temperature=0.7)

    tools = [
        Tool(name="Order Status", func=fetch_order_status, description="Get order status using order ID."),
        Tool(name="Product Recommendations", func=recommend_products, description="Get product recommendations.")
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    return agent
