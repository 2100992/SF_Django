from django.db import models

# Create your models here.


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.TextField()
    description = models.TextField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='books',
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='books',
    )

    def __str__(self):
        return self.title
