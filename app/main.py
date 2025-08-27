from fastapi import FastAPI
import math
from .schema import Book


app = FastAPI()

@app.get('/')
def root():
    return {'message':'hello'}


@app.get('/sqrt')
def sqrt(numero: int):
    return math.sqrt(numero)

book_db = []

@app.post('/books')
def create_book(book: Book):
    book_id = len(book_db) + 1
    book_data = {"id": book_id, **book.model_dump()}
    book_db.append(book_data)
    return book_data



@app.get('/books')
def list_book():
    return book_db
