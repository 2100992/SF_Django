# Generated by Django 2.2.7 on 2019-12-03 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20191201_1348'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]
