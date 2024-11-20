from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from app.tools import fetch_order_status, recommend_products

def create_agent() -> agent :
    llm = ChatOpenAI(model="gpt-4", temperature=0.7)

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
