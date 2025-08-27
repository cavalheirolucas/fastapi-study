from fastapi import FastAPI
import math


app = FastAPI()

@app.get('/')
def root():
    return {'message':'hello'}


@app.get('/sqrt')
def sqrt(numero: int):
    return math.sqrt(numero)

