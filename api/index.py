from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Axie API is running"}

@app.get("/axie/{axie_id}")
def get_axie(axie_id: int):
    return {"axie_id": axie_id}
