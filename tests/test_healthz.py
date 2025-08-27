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

#.venv\Scripts\Activate.ps1

#uvicorn app.main:app --reload

#git init
#git branch -M main
#git add .
#git commit -m "Inicializa projeto FastAPI simples"
#git remote add origin https://github.com/SEU-USUARIO/fastapi-quickstart.git
#git push -u origin main
