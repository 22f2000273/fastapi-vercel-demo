from fastapi import FastAPI


import json
app = FastAPI()
with open("data.json") as f:
    students = json.load(f)

@app.get("/students")
def get_students():
    return students
