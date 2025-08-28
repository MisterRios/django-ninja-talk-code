from sqlmodel import Field, Relationship, SQLModel


class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)

    books: list["Book"] = Relationship(back_populates="author")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=255)
    price: float
    summary: str | None

    author_id: int | None = Field(default=None, foreign_key="author.id")
    author: Author | None = Relationship(back_populates="books")





class AuthorPublic(SQLModel):
    id: int
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)

    full_name: str

class BookPublic(SQLModel)
    id: int
    title: str = Field(max_length=255)
    price: float
    summary: str | None

    author_id: int | None = Field(default=None, foreign_key="author.id")
    author: AuthorPublic
