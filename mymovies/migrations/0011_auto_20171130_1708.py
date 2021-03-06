# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymovies', '0010_auto_20171130_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_genre',
            field=models.CharField(choices=[('H', 'History'), ('Cl', 'Classic'), ('SF', 'Sci-Fi'), ('R', 'Romance'), ('A', 'Action'), ('Co', 'Comedy'), ('S', 'Supernatural'), ('SH', 'Superhero'), ('Cr', 'Crime')], max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_genre2',
            field=models.CharField(choices=[('H', 'History'), ('Cl', 'Classic'), ('SF', 'Sci-Fi'), ('R', 'Romance'), ('A', 'Action'), ('Co', 'Comedy'), ('S', 'Supernatural'), ('SH', 'Superhero'), ('Cr', 'Crime')], default='NONE', max_length=200),
        ),
    ]
