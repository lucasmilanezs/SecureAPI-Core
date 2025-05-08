from fastapi import FastAPI
from src.routes import user, auth

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

app.include_router(user.router)
app.include_router(auth.router)