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


class User(models.Model):
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


class Drugmaker(models.Model):
    title = models.CharField(
        max_length=50,
        db_index=True,
    )
    full_name = models.CharField(
        max_length=150,
        db_index=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = make_unique_slug(Drugmaker, slugify(self.title))
        super(Drugmaker, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Medicament(models.Model):
    title = models.CharField(
        max_length=50,
        db_index=True,
    )
    drugmaker = models.ForeignKey(
        Drugmaker,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='medicament',
    )
    release_form = models.CharField(
        max_length=50,
        blank=True,
    )
    quantity = models.SmallIntegerField(null=True, blank=True,)
    unit = models.CharField(
        max_length=50,
        blank=True,
    )
    slug = models.SlugField(default='_', max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = make_unique_slug(Medicament, slugify(self.title))
        super(Medicament, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Item(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='item',
    )
    medicament = models.ForeignKey(
        Medicament,
        on_delete=models.DO_NOTHING,
        related_name='item'
    )
    for_friends = models.BooleanField(default=False)
    for_all = models.BooleanField(default=False)
    transfer_conditions = models.CharField(max_length=150, blank=True,)
