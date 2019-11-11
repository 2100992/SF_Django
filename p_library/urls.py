from django.urls import path
from django.contrib import admin
from .views import AuthorEdit, AuthorList
# from my_site.urls import urlpatterns

app_name = 'p_library'

urlpatterns = [
    path('author/create/', AuthorEdit.as_view(), name='author_create'),
    path('authors/', AuthorList.as_view(), name='author_list')
]