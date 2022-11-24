from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def homePage():
    return {"test": "Es ist ein Test"}