# Generated by Django 2.2.7 on 2019-11-19 12:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(default='_', max_length=150, unique=True)),
                ('birth_year', models.SmallIntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=2, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(default='_', max_length=150, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('year_release', models.SmallIntegerField(blank=True, null=True)),
                ('copy_count', models.SmallIntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('author', models.ManyToManyField(related_name='book', to='p_library.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('slug', models.SlugField(default='_', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(default='_', max_length=150, unique=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('library_card', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(default='_', max_length=150, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=2, null=True)),
                ('tag', models.ManyToManyField(blank=True, related_name='publisher', to='p_library.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='BooksCopy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='books_copy', to='p_library.Book')),
                ('holder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='books_copy', to='p_library.User')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='p_library.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='book', to='p_library.Tag'),
        ),
        migrations.AddField(
            model_name='author',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='author', to='p_library.Tag'),
        ),
    ]
