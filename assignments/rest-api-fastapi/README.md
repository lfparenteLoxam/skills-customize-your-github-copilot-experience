# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using Python's FastAPI framework. You will create endpoints to manage a simple book catalog, learning how to define routes, validate data with Pydantic models, and handle errors properly.

## 📝 Tasks

### 🛠️ Task 1: Create a Basic FastAPI App

#### Description
Set up a FastAPI application with a root endpoint and a GET endpoint that returns a list of books from an in-memory store.

#### Requirements
Completed program should:

- Import and instantiate a `FastAPI` app
- Define a `GET /` endpoint that returns a welcome message
- Define a `GET /books` endpoint that returns all books as a list
- Each book should have at least `id`, `title`, and `author` fields


### 🛠️ Task 2: Add Data Validation with Pydantic

#### Description
Use Pydantic models to validate incoming data and define a `POST /books` endpoint to add new books to the catalog.

#### Requirements
Completed program should:

- Define a `Book` Pydantic model with `id` (int), `title` (str), `author` (str), and `year` (int) fields
- Define a `POST /books` endpoint that accepts a `Book` in the request body
- Append the new book to the in-memory list and return it with a `201` status code
- Reject requests with missing or wrong-type fields automatically via Pydantic validation


### 🛠️ Task 3: Path Parameters and Error Handling

#### Description
Add endpoints that use path parameters to retrieve or delete a specific book, and return proper HTTP errors when a book is not found.

#### Requirements
Completed program should:

- Define a `GET /books/{book_id}` endpoint that returns the book with the matching `id`
- Raise an `HTTPException` with status code `404` and a descriptive message when the book is not found
- Define a `DELETE /books/{book_id}` endpoint that removes the book and returns a confirmation message
- Also raise a `404` error in DELETE when the book does not exist


### 🛠️ Task 4 (Stretch): Update a Book with PUT

#### Description
Add a `PUT /books/{book_id}` endpoint to update an existing book's data.

#### Requirements
Completed program should:

- Accept a `Book` body and replace the matching book in the list
- Return the updated book on success
- Raise a `404` error if the book does not exist
- Preserve the original `id` even if the request body contains a different value
