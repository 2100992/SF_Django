from codecs import register
from django.contrib import admin

from p_library.models import Author, Book, BooksCopy, LibraryUser, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('country',)
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('ISBN', 'title', 'publisher')
    # fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price')

@admin.register(Publisher)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    pass

@admin.register(LibraryUser)
class LibraryUserUserAdmin(admin.ModelAdmin):
    pass

@admin.register(BooksCopy)
class BooksCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'holder')
    pass

# Register your models here.
