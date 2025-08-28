from books.api import router as books_router
from ninja import NinjaAPI

api = NinjaAPI(urls_namespace="api")

api.add_router("/books/", books_router)
