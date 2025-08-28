from books.models import Book
from books.schemas import BookSchema
from django.http import Http404
from ninja import Router

router = Router()


@router.get("/{id}", response=BookSchema, url_name="single_book")
async def get_single_book(request, id):
    try:
        book = await Book.objects.select_related("author").aget(id=id)
        if not book:
            raise Http404("Book not found")
    except Book.DoesNotExist:
        raise Http404("Book not found")
    else:
        return book


@router.get("/", response=list[BookSchema], url_name="all_books")
async def get_all_books(request):
    return [
        book async for book in Book.objects.select_related("author").order_by("title")
    ]
