from fastapi import FastAPI
from src.routes import user

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(user.router)