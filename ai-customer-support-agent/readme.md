```
ROOT_FOLDER/
├── app/
│   ├── __init__.py
│   ├── main.py          # Entry point for the application
│   ├── tools.py         # All tools (e.g., fetch_order_status, recommend_products)
│   ├── config.py        # Configuration (e.g., API keys, environment variables)
│   ├── agent.py         # Agent initialization and setup
│   ├── requirements.txt # Python dependencies
├── Dockerfile           # Docker build instructions
├── docker-compose.yml   # (Optional) Compose file for multi-container setups
├── .env                 # Environment variables
└── README.md            # Documentation
```

# Build and Run the container

```bash
docker build -t langchain-app .
docker run -p 5000:5000 langchain-app
```
## Test the api
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"query": "What is the status of order 12345?"}' http://localhost:5000/query
```
### Expected Response 
```json
{
  "response": "The order 12345 has shipped."
}
```
Happy Hunting!!! 