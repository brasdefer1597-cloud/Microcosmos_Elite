from fastapi import FastAPI
import json
import os

app = FastAPI()
DATA_PATH = "/data/sesgo.json"

@app.get("/status")
def get_status():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    return {"error": "No data"}
