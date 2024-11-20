from flask import Flask, request, jsonify
from agent import create_agent

app = Flask(__name__)
agent = create_agent()

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    user_query = data.get("query", "")
    if not user_query:
        return jsonify({"error": "Query not provided"}), 400

    try:
        response = agent.invoke(user_query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
