from codecs import register
from django.contrib import admin
from django.contrib.auth.models import User

from p_library.models import *

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

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'library_card')

@admin.register(BooksCopy)
class BooksCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'holder')
    readonly_fields = ('uuid',)
    # fields = ('book', 'holder', 'notes')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

# Unregister the provided model admin
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
