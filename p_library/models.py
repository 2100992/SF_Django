from django.db import models

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='books',
    )

    def __str__(self):
        return self.title


class LibraryUser(models.Model):
    # Таблица пользователей библиотеки
    full_name = models.TextField()
    library_card = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.full_name


class BooksCopy(models.Model):
    # В этой таблице будем хранить информацию о экземплярах книг
    # в каком они состоянии
    # у кого находятся (если ни у кого, значит в библиотеке)
    book = models.ForeignKey(
        Book,
        on_delete=models.DO_NOTHING,
        related_name='books_copy',
    )
    holder = models.ForeignKey(
        LibraryUser,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='books_copy'
    )
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.book.title

