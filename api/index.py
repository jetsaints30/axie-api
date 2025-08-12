from fastapi import FastAPI
import requests

app = FastAPI()

GRAPHQL_URL = "https://graphql-gateway.axieinfinity.com/graphql"

@app.get("/")
def home():
    return {"message": "Axie API is running"}

@app.get("/axie/{axie_id}")
def get_axie(axie_id: int):
    query = """
    query GetAxie($axieId: ID!) {
      axie(axieId: $axieId) {
        id
        bodyParts {
          name
          type
        }
      }
    }
    """
    variables = {"axieId": str(axie_id)}

    response = requests.post(GRAPHQL_URL, json={"query": query, "variables": variables})
    
    if response.status_code != 200:
        return {"error": "Failed to fetch from Axie Infinity API"}

    data = response.json()

    try:
        parts = data["data"]["axie"]["bodyParts"]
        return {"axie_id": axie_id, "bodyParts": parts}
    except:
        return {"error": "Axie not found or invalid response"}
