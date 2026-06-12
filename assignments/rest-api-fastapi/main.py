from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory book store
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
]


# TODO: Task 2 — Define a Book Pydantic model with id, title, author, and year fields
# class Book(BaseModel):
#     ...


# TODO: Task 1 — Add a GET / endpoint that returns a welcome message
@app.get("/")
def root():
    pass


# TODO: Task 1 — Add a GET /books endpoint that returns all books
@app.get("/books")
def get_books():
    pass


# TODO: Task 2 — Add a POST /books endpoint that accepts a Book body
# Use status_code=201 to return HTTP 201 Created
# @app.post("/books", status_code=201)
# def create_book(book: Book):
#     pass


# TODO: Task 3 — Add a GET /books/{book_id} endpoint
# Raise HTTPException(status_code=404) if the book is not found
# @app.get("/books/{book_id}")
# def get_book(book_id: int):
#     pass


# TODO: Task 3 — Add a DELETE /books/{book_id} endpoint
# @app.delete("/books/{book_id}")
# def delete_book(book_id: int):
#     pass


# TODO: Task 4 (Stretch) — Add a PUT /books/{book_id} endpoint
# @app.put("/books/{book_id}")
# def update_book(book_id: int, book: Book):
#     pass
