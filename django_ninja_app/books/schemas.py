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


# from pydantic.json import pydantic_encoder
# from pydantic import BaseModel
# class AuthorPublic(BaseModel)
# id: int
# first_name: str
# last_name: str
# full_name: str
#
# def json(self, **kwargs):
#     dict_data = self.dict()
#     dict_data["full_name"] = f"{self.first_name} {self.last_name}"
#     return pyjson.dumps(dict_data, default=pydantic_encoder, **kwargs)


# class BookSchema(BaseModel):
#     title: str
#     price: Decimal
#     summary: str
#     author: AuthorSchema
