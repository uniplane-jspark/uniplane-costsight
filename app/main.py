from fastapi import FastAPI

app = FastAPI(title="uniplane-costsight")

@app.get("/health")
def health():
    return {"status": "ok", "service": "uniplane-costsight"}
