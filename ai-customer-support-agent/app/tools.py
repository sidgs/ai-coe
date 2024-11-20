from langchain.tools import tool

@tool
def fetch_order_status(order_id: str) -> str:
    """
    Fetch the status of an order based on the order ID.
    """
    mock_database = {
        "12345": "Order shipped",
        "67890": "Order processing",
        "54321": "Order delivered",
    }
    return mock_database.get(order_id, "Order ID not found")


@tool
def recommend_products(category: str) -> str:
    """
    Recommend products based on a category.
    """
    recommendations = {
        "electronics": ["Smartphone", "Laptop", "Smartwatch"],
        "books": ["AI for Beginners", "LangChain Essentials", "Python Mastery"],
    }
    return ", ".join(recommendations.get(category.lower(), ["No recommendations found."]))
