from books.models import Book
from books.schemas import BookSchema
from ninja import Router

from django.shortcuts import get_object_or_404

router = Router()


@router.get("/{id}", response=BookSchema, url_name="single_book")
def get_single_book(request, id):
    return get_object_or_404(Book, pk=id)


@router.get("/", response=list[BookSchema], url_name="all_books")
def get_all_books(request):
    return Book.objects.order_by("title")
