from fastapi import FastAPI
import requests

app = FastAPI()

GRAPHQL_URL = "https://graphql-gateway.axieinfinity.com/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/110.0.0.0 Safari/537.36"
}

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

    response = requests.post(GRAPHQL_URL, headers=HEADERS, json={"query": query, "variables": variables})
    
    if response.status_code != 200:
        return {"error": f"Failed to fetch from Axie Infinity API: {response.status_code}"}

    data = response.json()

    try:
        parts = data["data"]["axie"]["bodyParts"]
        return {"axie_id": axie_id, "bodyParts": parts}
    except:
        return {"error": "Axie not found or invalid response"}
