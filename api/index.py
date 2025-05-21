from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()

STUDENT_MARKS = {
    "vb": 47,
    "bl2fduay": 9,
    "mlgrreraqw": 2,
    "yzxy79": 70,
    "bek6trx5": 62,
    "yjg": 35,
    "kppzdmu4c": 47,
    "nbnw4jsz": 72,
    "o": 12,
    "akqxftcfub": 0
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# This now handles GET requests to /api?name=...
@app.get("/")
async def get_marks(name: list[str] = Query(..., description="One or more student keys")):
    return {"marks": [STUDENT_MARKS.get(n.lower()) for n in name]}

handler = Mangum(app)
