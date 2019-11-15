from sys import prefix
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from p_library.models import Book, Author, Publisher
from django.template import loader
from p_library.forms import AuthorForm, BookForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect

# Create your views here.


def library(request):
    template = loader.get_template('p_library/index.html')
    # books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {
        "title": 'Моя библиотека',
        'books': books,
    }
    return HttpResponse(template.render(biblio_data, request))


# def books(request):
#     template = loader.get_template('p_library/books.html')
#     # books_count = Book.objects.all().count()
#     books = Book.objects.all()
#     biblio_data = {
#         "title": 'Моя библиотека',
#         'books': books,
#     }
#     return HttpResponse(template.render(biblio_data, request))

def books(request):
    books = Book.objects.all()
    biblio_data = {
        "title": 'Моя библиотека',
        'books': books,
    }
    return render(request, 'p_library/books.html', context=biblio_data)


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/library/books/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/library/books/')
            book.copy_count += 1
            book.save()
        return redirect('/library/books/')
    else:
        return redirect('/library/books/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/library/books/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/library/books/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/library/books/')
    else:
        return redirect('/books/')


def authors(request):
    template = loader.get_template('p_library/authors.html')
    authors = Author.objects.all()

    for author in authors:
        author.book_counter = Book.objects.filter(author=author).count()

    authors_data = {
        "title": 'Авторы',
        'authors': authors,
    }
    return HttpResponse(template.render(authors_data, request))


def publisher(request):
    template = loader.get_template('p_library/publishers.html')
    # books_count = Book.objects.all().count()
    publishers = Publisher.objects.all()  # .prefetch_related('books')

    # for publisher in publishers:
    #     publisher.books = Book.objects.filter(publisher=publisher)

    publishers_data = {
        "title": 'Издательства',
        'publishers': publishers,
    }
    return HttpResponse(template.render(publishers_data, request))


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    # success_url = '/library/authors/'
    success_url = reverse_lazy('p_library:authors')
    template_name = 'p_library/a_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'p_library/a_list.html'

    # def __init__(self, *args, **kwargs):
    #     print(self)


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(
            request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:authors'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
    return render(request, 'p_library/authors_manage.html', {'author_formset': author_formset})


def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=1)
    BookFormSet = formset_factory(BookForm, extra=1)
    if request.method == 'POST':
        author_formset = AuthorFormSet(
            request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(
        request,
        'p_library/books_authors_manage.html',
        {
            'author_formset': author_formset,
            'book_formset': book_formset,
        }
    )

def book_detail(request, slug):
    books = Book.objects.filter(slug__iexact=slug)
    if books.count() == 1:
        book_data = {
            'title': books.first().title,
            'book': books.first()
        }
        return render(request, 'p_library/book.html', context=book_data)
    else:
        return HttpResponseNotFound('<h1>No Page Here</h1>')