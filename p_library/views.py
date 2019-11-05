from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from p_library.models import Book, Author
from django.template import loader

# Create your views here.

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    # books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {
        "title": 'мою библиотеку',
        'books': books,
    }
    return HttpResponse(template.render(biblio_data))