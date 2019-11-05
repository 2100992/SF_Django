from django.contrib import admin

from p_library.models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('country',)
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('ISBN', 'title', 'author')
    # fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price')



# Register your models here.
