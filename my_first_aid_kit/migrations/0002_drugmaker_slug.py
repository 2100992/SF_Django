# Generated by Django 2.2.7 on 2019-11-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_aid_kit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugmaker',
            name='slug',
            field=models.SlugField(default='_', unique=True),
        ),
    ]
