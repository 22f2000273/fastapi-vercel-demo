# ✅ Correct: Convert FastAPI to Vercel-compatible ASGI handler
from fastapi import FastAPI
from mangum import Mangum  # ASGI adapter

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Vercel"}

handler = Mangum(app)  # ✅ Vercel uses this
