from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
        "books" : Book.objects.all(),
        }
    return render(request, "index.html", context)

def authors(request):
    context = {
        "authors" : Author.objects.all(),
        }
    return render(request, "authors.html", context)

def add_book(request):
    book = Book.objects.create(title = request.POST['title'],desc = request.POST['desc'])
    return redirect(f'/books/{book.id}')

def add_author(request):
    author = Author.objects.create(first_name = request.POST['fname'],last_name = request.POST['lname'],note = request.POST['notes'])
    return redirect(f'/authors/{author.id}')

def book_info(request, book_id):
    book_id = int(book_id)  
    books = Book.objects.get(id = book_id)
    show = Author.objects.exclude(books=books)

    context = {
        "books" : books,
        "authors": books.authors.all().values("first_name","last_name"),
        "all_books" : Book.objects.all(),
        "all_authors": show,
    }
    return render(request, "book_info.html", context)

def author_info(request, author_id):
    author_id = int(author_id)  
    authors = Author.objects.get(id = author_id)
    show = Book.objects.exclude(authors = authors)
    
    context = {
        "authors" : authors,
        "books": authors.books.all().values("title"),
        "all_books": show,
    }
    return render(request, "author_info.html", context)

def join_author(request):
    info = request.POST['book_info']
    bookInfo = Book.objects.get(id = info)
    newauthor = Author.objects.get(id = request.POST['addauthor'])
    bookInfo.authors.add(newauthor)
    return redirect(f'/books/{request.POST["book_info"]}', info)

def join_book(request):
    info = request.POST['author_info']
    authorInfo = Author.objects.get(id = info)
    newbook = Book.objects.get(id = request.POST['addbook'])
    authorInfo.books.add(newbook)
    return redirect(f'/authors/{request.POST["author_info"]}', info) 