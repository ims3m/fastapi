from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = {
    '1': {'title': '1984', 'author': 'George Orwell'},
    '2': {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    '3': {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
}

@app.get("/get_books")
async def get_books():
    return BOOKS

@app.get("/get_book/{book_id}")
async def get_book_by_id(book_id: str):
    book = BOOKS.get(book_id)
    if book:
        return book
    return {"error": "Book not found"}

@app.get("/book/{dynamic_block}")
async def get_dynamic(dynamic_block: str):
    return {"value": dynamic_block}

@app.put("/update_book")
async def update_book(update_book = Body()):
    print(f'{update_book}')
    _id = update_book.get("id")
    BOOKS[_id] = update_book.get("data", {})
    return BOOKS

@app.delete("/delete_book/{book_id}")
async def delete_book(book_id: str):
    if book_id in BOOKS:
        del BOOKS[book_id]
        return {"message": "Book deleted"}
    return {"error": "Book not found"}