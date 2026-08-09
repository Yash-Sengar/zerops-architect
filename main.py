from fastapi import FastAPI

app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    prompt = data.get("prompt", "")
    # Add AI processing / LLM call here
    return {"status": "success", "response": f"AI processed: {prompt}"}
