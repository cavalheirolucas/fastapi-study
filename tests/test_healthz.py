from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/hello")
def hello():
    return {"msg": "Bem-vindo!"}

@app.get("/ping")
def ping():
    return {"msg": "pong"}

@app.get("/sum")
def soma(a: int, b: int):
    return {"resultado": a + b}

@app.get("/reverse")
def reverse(word: str):
    return {"resultado": word[::-1]}

#.venv\Scripts\Activate.ps