from p_library.models import Book
from p_library.views import BookDetail, AuthorDetail, PublisherDetail, UserDetail
from django.urls import path
from . import views
# from my_site.urls import urlpatterns

app_name = 'p_library'

urlpatterns = [
    path('', views.library),

    path('books/', views.Books.as_view(), name='books_list_url'),
    path('book/<str:slug>/', views.BookDetail.as_view(), name='book_detail_url'),

    path('book_author/create_many/', views.books_authors_create_many, name='books_authors_create_many'),

    path('authors/', views.Authors.as_view(), name='authors_list_url'),

    path('author/create/', views.AuthorEdit.as_view(), name='author_create'),
    path('author/create_many/', views.author_create_many, name='author_create_many'),

    path('author/<str:slug>/', views.AuthorDetail.as_view(), name='author_detail_url'),

    path('publishers/', views.Publishers.as_view(), name='publishers_list_url'),
    path('publisher/<str:slug>/', views.PublisherDetail.as_view(), name='publisher_detail_url'),

    path('f_authors/', views.AuthorList.as_view(), name='authors_list'),

    path('users/', views.Users.as_view(), name='users_list_url'),
    path('user/<str:slug>/', views.UserDetail.as_view(), name='user_detail_url'),

    path('tags/', views.Tags.as_view(), name='tags_list_url'),
    path('tag/<str:slug>/', views.TagDetail.as_view(), name='tag_detail_url'),

    path('books-copies/', views.BooksCopies.as_view(), name='copies_list_url'),
    path('books-copy/<str:uuid>/', views.BooksCopyDetail.as_view(), name='copy_detail_url'),
]