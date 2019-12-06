from sys import prefix
from p_library.models import *
from p_library.forms import AuthorForm, BookForm, ProfileCreationForm

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.http.response import HttpResponseRedirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.template import loader

from django.views.generic import CreateView, ListView, View, FormView
from django.urls import reverse_lazy, reverse
from django.forms import formset_factory

from .utils import ObjectDetailMixin, ObjectsListMixin

from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


def library(request):
    template = loader.get_template('p_library/index.html')
    # books_count = Book.objects.all().count()
    books = Book.objects.all()
    context = {
        "title": 'Моя библиотека',
        'books': books,
    }
    if request.user.is_authenticated:
        context['username'] = request.user.username
        if UserProfile.objects.filter(user=request.user).count():
            context['age'] = f"Возраст посчитаем из дня рождения - {UserProfile.objects.get(user=request.user).birth_date} но потом"
    return HttpResponse(template.render(context, request))


# def books(request):
#     template = loader.get_template('p_library/books.html')
#     # books_count = Book.objects.all().count()
#     books = Book.objects.all()
#     biblio_data = {
#         "title": 'Моя библиотека',
#         'books': books,
#     }
#     return HttpResponse(template.render(biblio_data, request))

# def books(request):
#     books = Book.objects.all()
#     biblio_data = {
#         "title": 'Моя библиотека',
#         'books': books,
#     }
#     return render(request, 'p_library/books.html', context=biblio_data)


class Books(View):
    model = Book
    template = 'p_library/books.html'
    title = 'Книги'

    def get(self, request):
        books = get_list_or_404(self.model)
        for book in books:
            book.available_copies = book.books_copy.all().filter(holder=None).count()

        context = {
            self.model.__name__.lower(): books
        }

        if request.user.is_authenticated:
            context['username'] = request.user.username
            if UserProfile.objects.filter(user=request.user).count():
                        context['age'] = f"Возраст посчитаем из дня рождения - {UserProfile.objects.get(user=request.user).birth_date} но потом"

        return render(request, self.template, context=context)


class BooksCopies(ObjectsListMixin, View):
    model = BooksCopy
    template = 'p_library/bookscopies.html'
    title = 'Экземпляры книг'


class Authors(ObjectsListMixin, View):
    model = Author
    template = 'p_library/authors.html'
    title = 'Авторы'


class UserProfiles(ObjectsListMixin, View):
    model = UserProfile
    template = 'p_library/users.html'
    title = 'Пользователи'


class Tags(ObjectsListMixin, View):
    model = Tag
    template = 'p_library/tags.html'
    title = 'Тэги'


class Publishers(ObjectsListMixin, View):
    model = Publisher
    template = 'p_library/publishers.html'
    title = 'Издатели'


# def book_increment(request):
#     if request.method == 'POST':
#         book_id = request.POST['id']
#         if not book_id:
#             return redirect('/library/books/')
#         else:
#             book = Book.objects.filter(id=book_id).first()
#             if not book:
#                 return redirect('/library/books/')
#             book.copy_count += 1
#             book.save()
#         return redirect('/library/books/')
#     else:
#         return redirect('/library/books/')


# def book_decrement(request):
#     if request.method == 'POST':
#         book_id = request.POST['id']
#         if not book_id:
#             return redirect('/library/books/')
#         else:
#             book = Book.objects.filter(id=book_id).first()
#             if not book:
#                 return redirect('/library/books/')
#             if book.copy_count < 1:
#                 book.copy_count = 0
#             else:
#                 book.copy_count -= 1
#             book.save()
#         return redirect('/library/books/')
#     else:
#         return redirect('/books/')


# def authors(request):
#     template = loader.get_template('p_library/authors.html')
#     authors = Author.objects.all()

#     for author in authors:
#         author.book_counter = Book.objects.filter(author=author).count()

#     authors_data = {
#         "title": 'Авторы',
#         'authors': authors,
#     }
#     return HttpResponse(template.render(authors_data, request))


# def publisher(request):
#     template = loader.get_template('p_library/publishers.html')
#     # books_count = Book.objects.all().count()
#     publishers = Publisher.objects.all()  # .prefetch_related('books')

#     # for publisher in publishers:
#     #     publisher.books = Book.objects.filter(publisher=publisher)

#     publishers_data = {
#         "title": 'Издательства',
#         'publishers': publishers,
#     }
#     return HttpResponse(template.render(publishers_data, request))


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    # success_url = '/library/authors/'
    success_url = reverse_lazy('p_library:authors_list_url')
    template_name = 'p_library/a_edit.html'


'''
class AuthorList(ListView):
    model = Author
    template_name = 'p_library/a_list.html'

    # def __init__(self, *args, **kwargs):
    #     print(self)
'''


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

# Далее две эквивалентные вьюхи
# def и class based
# для работы воторой нежно urls внести изменение


# def book_detail(request, slug):
#     books = Book.objects.filter(slug__iexact=slug)
#     if books.count() == 1:
#         book_data = {
#             'title': books.first().title,
#             'book': books.first()
#         }
#         return render(request, 'p_library/book.html', context=book_data)
#     else:
#         return HttpResponseNotFound('<h1>No Page Here</h1>')

# Эту вьюху заменили на аналогичную с миксинами
# class BookDetail(View):
#     def get(self, request, slug):
#         book = get_object_or_404(Book, slug__iexact=slug)
#         return render(request, 'p_library/book.html', context={'book': book})


class BookDetail(ObjectDetailMixin, View):
    model = Book
    template = 'p_library/book.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'p_library/tag.html'


class UserDetail(ObjectDetailMixin, View):
    model = UserProfile
    template = 'p_library/user.html'


class PublisherDetail(ObjectDetailMixin, View):
    model = Publisher
    template = 'p_library/publisher.html'


class AuthorDetail(ObjectDetailMixin, View):
    model = Author
    template = 'p_library/author.html'


class BooksCopyDetail(View):
    model = BooksCopy
    template = 'p_library/bookscopy.html'

    def get(self, request, uuid):
        obj = get_object_or_404(self.model, uuid=uuid)
        context = {
            self.model.__name__.lower(): obj
        }

        if request.user.is_authenticated:
            context['username'] = request.user.username
            if UserProfile.objects.filter(user=request.user).count():
                        context['age'] = f"Возраст посчитаем из дня рождения - {UserProfile.objects.get(user=request.user).birth_date} но потом"

        return render(request, self.template, context=context)


class Login(LoginView):
    template_name = 'p_library/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        elif self.request.user.is_superuser:
            return '/admin/'
            # return reverse('admin')   # почему-то не работает
        else:
            return reverse('p_library:library_url')

    # redirect_field_name = reverse('p_library:library_url')


class Logout(LogoutView):
    next_page = '/p_library/'

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             auth.login(request, form.get_user())
#             return HttpResponseRedirect(reverse_lazy('p_library:library_url'))
#         else:
#             # ToDo:
#             # Добавить сообщение о ошибке лониг/пароль
#             return HttpResponseRedirect(reverse_lazy('p_library:library_url'))
#     else:
#         context = {'form': AuthenticationForm()}
#         return render(request, 'p_library/login.html', context)


# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse_lazy('p_library:library_url'))


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name='p_library/register.html'
    success_url=reverse_lazy('p_library:create_user_profile_url')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(
            username=username, password=raw_password))
        return super(RegisterView, self).form_valid(form)


class CreateUserProfile(FormView):
    form_class = ProfileCreationForm
    template_name = 'p_library/profile-create.html'
    success_url = reverse_lazy('p_library:library_url')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('p_library:login_url'))
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CreateUserProfile, self).form_valid(form)
