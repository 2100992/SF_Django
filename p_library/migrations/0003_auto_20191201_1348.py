# Generated by Django 2.2.7 on 2019-12-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_book_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='p_library/books/covers/%Y/%m/%d'),
        ),
    ]
