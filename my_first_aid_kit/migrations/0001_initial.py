# Generated by Django 2.2.7 on 2019-11-26 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugmaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('full_name', models.CharField(db_index=True, max_length=150, unique=True)),
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
            name='Medicament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('release_form', models.CharField(blank=True, max_length=50)),
                ('quantity', models.SmallIntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(default='_', unique=True)),
                ('drugmaker', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='medicament', to='my_first_aid_kit.Drugmaker')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_friends', models.BooleanField(default=False)),
                ('for_all', models.BooleanField(default=False)),
                ('transfer_conditions', models.CharField(blank=True, max_length=150)),
                ('medicament', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='item', to='my_first_aid_kit.Medicament')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='item', to='my_first_aid_kit.User')),
            ],
        ),
    ]