from books.models import Author, Book
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewBookForm, BorrowBookForm
from django.contrib import messages



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

@login_required
def show(req, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if req.method == 'POST':
        form = BorrowBookForm(req.POST)
        if form.is_valid():
            if book.borrower == None:
                book.borrower = req.user
            else:
                book.borrower = None 
            book.save()
            return redirect("books-show", book_id=book_id)
    else:
        form = BorrowBookForm(initial={'borrower': req.user})
        data = { "book": book,
                "form": form
                
        }
    return render(req, 'books/book.html', data)





def new_book(req):
    if req.method == 'POST':
        form = NewBookForm(req.POST)
        if form.is_valid():
            book = form.save()
            book_id = book.id
            title = form.cleaned_data.get('title')
            messages.success(req, f'{title} has been added to the library!')
            return redirect('books-show', book_id=book_id)
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(req, 'books/new.html', data)


def not_found_404(req, exception):
    return HttpResponse(f"<h1>Invalid Page 404</h1>")

def server_error_500(req):
    return HttpResponse(f"<h1>Invalid Page 500</h1>")