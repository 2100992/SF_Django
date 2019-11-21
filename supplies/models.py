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


class Nomenclature(models.Model):
    name = models.CharField(
        max_length=50,
        db_index=True,
    )
    title = models.CharField(
        max_length=150,
        db_index=True,
        unique=True
    )
    slug = models.SlugField(
        default='_',
        max_length=50,
        unique=True
    )


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = make_unique_slug(Tag, slugify(self.title))
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
