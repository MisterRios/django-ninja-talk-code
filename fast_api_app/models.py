from sqlmodel import Field, Relationship, SQLModel


class AuthorBase(SQLModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)


class Author(AuthorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    books: list["Book"] = Relationship(back_populates="author")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class AuthorPublic(AuthorBase):
    id: int
    full_name: str


class BookBase(SQLModel):
    title: str = Field(max_length=255)
    price: float
    summary: str | None

    author_id: int | None = Field(default=None, foreign_key="author.id")


class Book(BookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author: Author | None = Relationship(back_populates="books")


class BookPublic(BookBase):
    id: int
    author: AuthorPublic


class CardBase(SQLModel):
    name: str = Field(max_length=50)
    creator: str = Field(max_length=100)
    price: float


class Card(CardBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class CardPublic(CardBase):
    id: int
