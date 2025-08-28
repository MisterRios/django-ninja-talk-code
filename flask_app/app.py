from typing import Optional

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    column_property,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column()
    summary: Mapped[Optional[str]] = mapped_column(Text)

    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    author: Mapped["Author"] = relationship(back_populates="book")


class Author(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))

    full_name: Mapped[str] = column_property(first_name + " " + last_name)

    book: Mapped["Book"] = relationship(back_populates="author")


class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    creator: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column()


with app.app_context():
    db.create_all()


def serialize_book(book):
    book_dict = {
        "id": book.id,
        "title": book.title,
        "price": book.price,
        "summary": book.summary,
        "author": {
            "id": book.author.id,
            "full_name": book.author.full_name,
        },
    }
    return book_dict


@app.route("/api/books/")
def get_all_books():
    select_statement = db.select(Book).order_by(Book.title)
    books = db.session.execute(select_statement).all()

    # each instance is a tuple with one element
    return jsonify([serialize_book(book[0]) for book in books])


@app.route("/api/books/<int:id>")
def get_single_book(id):
    book = db.get_or_404(Book, id)
    return jsonify(serialize_book(book))
