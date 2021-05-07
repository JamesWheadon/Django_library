from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books-index'),
    path('books/<int:book_id>/', views.show, name='books-show'),
    path('books/new', views.new_book, name='books-new')
    
]