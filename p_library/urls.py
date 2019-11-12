from django.urls import path
from . import views
# from my_site.urls import urlpatterns

app_name = 'p_library'

urlpatterns = [
    path('', views.library),
    path('books/', views.books, name='books'),
    path('books/book_increment/', views.book_increment),
    path('books/book_decrement/', views.book_decrement),
    path('book_author/create_many/', views.books_authors_create_many, name='books_authors_create_many'),
    path('authors/', views.authors, name='authors'),
    path('author/create/', views.AuthorEdit.as_view(), name='author_create'),
    path('author/create_many/', views.author_create_many, name='author_create_many'),
    path('publishers/', views.publisher),
    path('f_authors/', views.AuthorList.as_view(), name='author_list'),
]