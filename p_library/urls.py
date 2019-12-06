from p_library.models import Book
from p_library.views import library
from p_library.views import Books, BookDetail
from p_library.views import Authors, AuthorDetail
from p_library.views import Publishers, PublisherDetail
from p_library.views import UserProfiles, UserDetail
from p_library.views import Tags, TagDetail
from p_library.views import BooksCopies, BooksCopyDetail
from p_library.views import Login, Logout
from p_library.views import RegisterView, CreateUserProfile

from django.urls import path
# from . import views
# from my_site.urls import urlpatterns

app_name = 'p_library'

urlpatterns = [
    path('', library,
        name='library_url'),

    path('books/', Books.as_view(),
        name='books_list_url'),
    path('book/<str:slug>/', BookDetail.as_view(),
        name='book_detail_url'),

    path('authors/', Authors.as_view(),
        name='authors_list_url'),
    path('author/<str:slug>/', AuthorDetail.as_view(),
        name='author_detail_url'),

    path('publishers/', Publishers.as_view(),
        name='publishers_list_url'),
    path('publisher/<str:slug>/', PublisherDetail.as_view(),
        name='publisher_detail_url'),

    path('users/', UserProfiles.as_view(),
        name='users_list_url'),
    path('user/<str:slug>/', UserDetail.as_view(),
        name='user_detail_url'),

    path('tags/', Tags.as_view(),
        name='tags_list_url'),
    path('tag/<str:slug>/', TagDetail.as_view(),
        name='tag_detail_url'),

    path('books-copies/', BooksCopies.as_view(),
        name='copies_list_url'),
    path('books-copy/<str:uuid>/', BooksCopyDetail.as_view(),
        name='copy_detail_url'),

    path('login/', Login.as_view(),
        name='login_url'),
    path('logout/', Logout.as_view(),
        name='logout_url'),

    path('register-user/', RegisterView.as_view(),
        name='register_user_url'),
    path('create-user-profile', CreateUserProfile.as_view(),
        name='create_user_profile_url'),
]

# path('book_author/create_many/', books_authors_create_many, name='books_authors_create_many'),
# path('author/create/', views.AuthorEdit.as_view(), name='author_create'),
# path('author/create_many/', views.author_create_many, name='author_create_many'),
# path('f_authors/', views.AuthorList.as_view(), name='authors_list'),
