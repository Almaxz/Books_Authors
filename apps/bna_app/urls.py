from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('books/add', views.add_book),
    path('authors/add', views.add_author),
    path('books/<book_id>', views.book_info),
    path('authors/<author_id>', views.author_info),
    path('join_author', views.join_author),
    path('join_book', views.join_book)
]
