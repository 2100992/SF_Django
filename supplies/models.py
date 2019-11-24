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


'''_______________________________________________________________________________'''


class Nomenclature(models.Model):
    # Тип изделия (микросхема, ТУ, отладочный модуль)
    products_type = models.CharField(max_length=50, blank=True,)
    # Условное обозначение изделия (дейтоновские 1892ВМ14Я, Салют-ЭЛ24ПМ2)
    simbol = models.CharField(max_length=50, blank=True,)
    # Внутренние наименования изделия (MCom-02, Салют-ЭЛ24ПМ)
    name = models.CharField(max_length=50, blank=True,)
    # Тип приемки (ОТК, ФК, ГК)
    control_type = models.CharField(max_length=50, blank=True,)
    # Наименование с учетом приемки и прочих особенностей
    # (Микросхема 1892ВМ14Я (ФК в нормальных климатических условиях))
    title = models.CharField(max_length=150, db_index=True, unique=True)
    slug = models.SlugField(default='_', max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    @property
    def new_slug(self):
        self.slug = make_unique_slug(Nomenclature, slugify(self.title[:45]))
        return self.slug

    def save(self, *args, **kwargs):
        if self.slug == '_':
            self.slug = make_unique_slug(
                Nomenclature, slugify(self.title[:45]))
        super(Nomenclature, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


'''_______________________________________________________________________________'''


class CompanyInfo(models.Model):
    # Краткое наименование компании (ООО "РиК")
    name = models.CharField(max_length=50, blank=True,)
    # Полное наименование компании (MCom-02, Салют-ЭЛ24ПМ)
    full_name = models.CharField(max_length=50, blank=True,)
    # Наименование с учетом приемки и прочих особенностей
    # (Микросхема 1892ВМ14Я (ФК в нормальных климатических условиях))
    title = models.CharField(max_length=150, db_index=True, unique=True,)
    country = models.CharField(max_length=50, blank=True,)
    city = models.CharField(max_length=50, blank=True,)
    address = models.CharField(max_length=150, blank=True,)
    slug = models.SlugField(default='_', max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    @property
    def new_slug(self):
        self.slug = make_unique_slug(CompanyInfo, slugify(self.title[:45]))
        return self.slug

    def save(self, *args, **kwargs):
        if self.slug == '_':
            self.slug = make_unique_slug(CompanyInfo, slugify(self.title[:45]))
        super(Nomenclature, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


'''_______________________________________________________________________________'''


class Item(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(
        Nomenclature, on_delete=models.DO_NOTHING, related_name='item')
    serial_number = models.CharField(max_length=50, blank=True,)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product.title


'''_______________________________________________________________________________'''


class Person(models.Model):
    name = models.CharField(max_length=50, blank=True,)
    surname = models.CharField(max_length=50, blank=True,)
    patronymic = models.CharField(max_length=50, blank=True,)
    company = models.ForeignKey(
    CompanyInfo, blank=True, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(default='_', max_length=50, unique=True)

    @property
    def new_slug(self):
        self.slug = make_unique_slug(Person, slugify((self.surname + self.name + self.patronymic)[:45]))
        return self.slug

    def save(self, *args, **kwargs):
        if self.slug == '_':
            self.slug = make_unique_slug(Person, slugify((self.surname + self.name + self.patronymic)[:45]))
        super(Nomenclature, self).save(*args, **kwargs)

    def __str__(self):
        return self.surname + self.name + self.patronymic

'''_______________________________________________________________________________'''


class Sale(models.Model):
    sales_number = models.SmallIntegerField(null=True, blank=True,)
    sales_date = models.DateField(auto_now_add=True)
    company = models.ForeignKey(CompanyInfo, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Nomenclature, on_delete=models.DO_NOTHING)
    quantity = models.SmallIntegerField(null=True, blank=True,)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True,)
    description = models.TextField(null=True, blank=True)

'''_______________________________________________________________________________'''
class Shipment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    sale = models.ForeignKey(Sale, on_delete=models.DO_NOTHING)

