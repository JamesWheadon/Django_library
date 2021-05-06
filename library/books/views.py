from books.models import Author, Book
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
"""books = [
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Life', 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
]"""

def index(req):
    """return_item = "<ul>"
    for book in Book.objects.all():
        book_item = f"<li>Title: {book.title}</li>"
        return_item += book_item
    return_item += "</ul>"
    return HttpResponse(return_item)"""
    data = { 'books': Book.objects.all() }
    return render(req, 'books/home.html', data)

def show(req, id):
    book = get_object_or_404(Book, pk=id)
    return HttpResponse(f"<h3>Author: {book.author.name}</h3><h3>Title: {book.title}</h3>")

def not_found_404(req, exception):
    return HttpResponse(f"<h1>Invalid Page 404</h1>")

def server_error_500(req):
    return HttpResponse(f"<h1>Invalid Page 500</h1>")