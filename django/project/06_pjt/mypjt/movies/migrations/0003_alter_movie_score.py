# Generated by Django 3.2.13 on 2022-10-07 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='score',
            field=models.FloatField(default=5),
        ),
    ]