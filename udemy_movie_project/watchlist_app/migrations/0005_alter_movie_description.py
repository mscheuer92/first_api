# Generated by Django 5.2.1 on 2025-06-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_alter_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
