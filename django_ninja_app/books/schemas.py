from books.models import Author, Book
from ninja import ModelSchema


class AuthorSchema(ModelSchema):
    full_name: str

    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name"]


class BookSchema(ModelSchema):
    author: AuthorSchema

    class Meta:
        model = Book
        fields = ["id", "title", "price", "summary", "author"]
