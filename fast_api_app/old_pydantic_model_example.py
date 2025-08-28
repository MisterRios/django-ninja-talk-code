from pydantic import BaseModel


class AuthorPublic(BaseModel):
    id: int
    first_name: str
    last_name: str


class BookPublic(BaseModel):
    id: int
    title: str
    price: float
    summary: str

    author: "AuthorPublic"
