# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymovies', '0003_auto_20171128_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_genre2',
            field=models.CharField(choices=[('H', 'History'), ('Cl', 'Classic'), ('SF', 'Sci-Fi'), ('R', 'Romance'), ('A', 'Action'), ('Co', 'Comedy'), ('S', 'Supernatural'), ('SH', 'Superhero')], default='NONE', max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_super_hero',
            field=models.CharField(choices=[('B', 'Batman'), ('SupM', 'Superman'), ('SpiM', 'Spiderman'), ('IM', 'Ironman'), ('T', 'Thor'), ('CA', 'Captain America'), ('H', 'Hulk'), ('W', 'Wolverine')], default='NONE', max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_tracks',
            field=models.CharField(default='NONE', max_length=500),
        ),
    ]
