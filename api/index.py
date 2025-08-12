from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Axie API is running"}

@app.get("/axie/{axie_id}")
def get_axie(axie_id: int):
    try:
        url = "https://graphql-gateway.axieinfinity.com/graphql"
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
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "errors" in data:
            return {"error": data["errors"]}

        return data["data"]["axie"]
    except Exception as e:
        return {"error": str(e)}
