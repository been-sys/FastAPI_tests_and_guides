from fastapi import FastAPI, HTTPException
import uvicorn
# BaseModel - это базовый класс pydantic, все основные взаимодействия происходят с ним
from pydantic import BaseModel

class NewBook(BaseModel):
    title: str
    author: str

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "AP",
        "author": "Mathu",
    },
    {
        "id": 2,
        "title": "AP2",
        "author": "Mathu2",
    },
]


@app.get("/books", tags=["Книги"], summary="Получить все книги")
def read_books():
    return books


@app.get("/books/{book_id}", tags=["Книги"], summary="Получить конкретную книгу")
def read_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

    return books[book_id]

@app.post("/books")
def create_book(new_book: NewBook):
    books.append({
        "id": len(books)+1,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {"success":"True", "message":"Книга успешно добавлена"}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
