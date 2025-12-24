from fastapi import Body, FastAPI
from pydantic import BaseModel


app = FastAPI()


BOOKS = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "description": "A novel set in the Roaring Twenties.",
        "rating": 5,
    },
    {
        "id": 2,
        "title": "To Kill a Mocking bird",
        "author": "Harper Lee",
        "description": "A novel about racial injustice in the Deep South.",
        "rating": 4,
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str = None
    rating: int = None


@app.get("/books")
async def get_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book : Book):
    new_book = Book(**book.dict())
    BOOKS.append(new_book)
    return BOOKS