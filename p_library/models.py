from django.db import models

import uuid
from slugify import slugify


def make_unique_slug(model, text, counter=0):
    str_counter = ''
    if counter:
        str_counter = str(counter)
    if model.objects.filter(slug=text+str_counter).count():
        counter += 1
        text = make_unique_slug(model, text, counter)
    return text + str_counter


# Create your models here.

class Tag(models.Model):
    title = models.CharField(
        max_length=50,
        db_index=True,
        unique=True
    )
    slug = models.SlugField(default='_', max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = make_unique_slug(Tag, slugify(self.title))
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(default='_', max_length=150, unique=True)
    birth_year = models.SmallIntegerField(null=True, blank=True,)
    country = models.CharField(max_length=2, null=True, blank=True,)
    description = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='author',
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = make_unique_slug(Author, slugify(self.full_name))
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(default='_', max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True,)
    tag = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='publisher',
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = make_unique_slug(Publisher, slugify(self.name))
        super(Publisher, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(default='_', max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)
    year_release = models.SmallIntegerField(null=True, blank=True,)
    copy_count = models.SmallIntegerField(null=True, blank=True,)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True,)
    author = models.ManyToManyField(Author, related_name='book')
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='books',
    )
    tag = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='book',
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = make_unique_slug(Book, slugify(self.title))
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class User(models.Model):
    # Таблица пользователей библиотеки
    full_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(default='_', max_length=150, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    library_card = models.CharField(
        max_length=13,
        null=True,
        blank=True,
        unique=True
    )
    description = models.TextField(null=True, blank=True,)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = make_unique_slug(User, slugify(self.full_name))
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class BooksCopy(models.Model):
    # В этой таблице будем хранить информацию о экземплярах книг
    # в каком они состоянии
    # у кого находятся (если ни у кого, значит в библиотеке)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(
        Book,
        on_delete=models.DO_NOTHING,
        related_name='books_copy',
    )
    holder = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='books_copy'
    )
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.book.title

