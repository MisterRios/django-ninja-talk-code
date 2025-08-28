from fastapi import FastAPI, HTTPException
from models import Author, AuthorPublic, Book, BookPublic, Card  # noqa: F401
from sqlalchemy.orm import selectinload
from sqlmodel import Session, SQLModel, create_engine, select

app = FastAPI()

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/api/books/{id}", response_model=BookPublic)
async def get_single_book(id):
    with Session(engine) as session:
        statement = select(Book).where(Book.id == id).options(selectinload(Book.author))
        book = session.exec(statement).one()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book


@app.get("/api/books", response_model=list[BookPublic])
async def get_all_books():
    with Session(engine) as session:
        select_statement = (
            select(Book).options(selectinload(Book.author)).order_by(Book.title)
        )
        books = session.exec(select_statement).all()
        return books
