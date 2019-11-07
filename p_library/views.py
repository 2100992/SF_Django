from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from p_library.models import Book, Author, Publisher
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    # books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {
        "title": 'Моя библиотека',
        'books': books,
    }
    return HttpResponse(template.render(biblio_data, request))


def books(request):
    template = loader.get_template('books.html')
    # books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {
        "title": 'Моя библиотека',
        'books': books,
    }
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/books/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/books/')
            book.copy_count += 1
            book.save()
        return redirect('/books/')
    else:
        return redirect('/books/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/books/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/books/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/books/')
    else:
        return redirect('/books/')

def authors(request):
    template = loader.get_template('authors.html')
    authors = Author.objects.all()

    for author in authors:
        author.book_counter = Book.objects.filter(author=author).count()

    authors_data = {
        "title": 'Авторы',
        'authors': authors,
    }
    return HttpResponse(template.render(authors_data, request))

def publisher(request):
    template = loader.get_template('publishers.html')
    # books_count = Book.objects.all().count()
    publishers = Publisher.objects.all()

    for publisher in publishers:
        publisher.books = Book.objects.filter(publisher=publisher)

    publishers_data = {
        "title": 'Издательства',
        'publishers': publishers,
    }
    return HttpResponse(template.render(publishers_data, request))
