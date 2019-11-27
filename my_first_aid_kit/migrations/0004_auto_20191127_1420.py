# Generated by Django 2.2.7 on 2019-11-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_aid_kit', '0003_auto_20191127_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveSubstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(default='_', unique=True)),
                ('tag', models.ManyToManyField(blank=True, related_name='active_substance', to='my_first_aid_kit.Tag')),
            ],
        ),
        migrations.RemoveField(
            model_name='medicament',
            name='active_substances',
        ),
        migrations.AddField(
            model_name='drugmaker',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='drugmaker', to='my_first_aid_kit.Tag'),
        ),
        migrations.AddField(
            model_name='item',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='item', to='my_first_aid_kit.Tag'),
        ),
        migrations.AddField(
            model_name='medicament',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='medicament', to='my_first_aid_kit.Tag'),
        ),
        migrations.AddField(
            model_name='pharmagroup',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='pharma_group', to='my_first_aid_kit.Tag'),
        ),
        migrations.DeleteModel(
            name='ActiveSubstances',
        ),
        migrations.AddField(
            model_name='medicament',
            name='active_substance',
            field=models.ManyToManyField(related_name='medicament', to='my_first_aid_kit.ActiveSubstance'),
        ),
    ]
