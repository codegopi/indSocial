from fastapi import FastAPI

app = FastAPI()

#this is a test
@app.get("/")
def homePage():
    return {"test": "Es ist ein Test"}