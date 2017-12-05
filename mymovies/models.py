from django.db import models
from django.utils import timezone
import datetime
from django.dispatch import receiver
from django.contrib.auth.models import User

import random



                

class Movie(models.Model):
        
    genre_dict = { 
      "History": "H", "Classic": "Cl", 'Sci-Fi': 'SF',
      'Romance': "R", 'Action': "A", "Comedy": "Co",
      "Supernatural": "S", "Superhero": "SH", "Crime": "Cr",
          "Drama": "D","Mystery": "M"

    }
        
        
    genre_dict2 = { 
      "History": "H", "Classic": "Cl", 'Sci-Fi': 'SF',
      'Romance': "R", 'Action': "A", "Comedy": "Co",
      "Supernatural": "S", "Superhero": "SH", "Crime": "Cr",
          "Drama": "D","Mystery": "M"

    }
        
    super_heroes = { 
      "Batman": "B", "Superman": "SupM", 'Spiderman': 'SpiM',
      'Ironman': "IM", 'Thor': "T", "Captain America": "CA",
      "Hulk": "H", "Wolverine": "W"

    }
    
    GENRE_CHOICES = [(code,label) for label,code in genre_dict.items()]
    GENRE_CHOICES2 = [(code,label) for label,code in genre_dict2.items()]
    SUPER_HEROES_CHOICES = [(code,label) for label,code in super_heroes.items()]
    
    topic_author = models.ForeignKey('auth.User')       
    movie_title = models.CharField(max_length=100)
    movie_trailer = models.CharField(max_length=85)
    movie_year = models.IntegerField(default=1996)
    movie_genre = models.CharField(max_length=200, choices=GENRE_CHOICES)
    movie_genre2 = models.CharField(max_length=200, choices=GENRE_CHOICES2, default='NONE')
    movie_super_heroes = models.CharField(max_length=200, choices=SUPER_HEROES_CHOICES, default='NONE')
    movie_description = models.TextField(blank=True)
    movie_staff = models.CharField(max_length=500)
    movie_staff2 = models.CharField(max_length=500,default='NONE')
    movie_image = models.ImageField(upload_to="movie_imgs", blank=True)
    movie_imdb = models.FloatField(default=10)
    movie_tracks = models.CharField(max_length=100, default='NONE')
        
        

    def __str__(self):
        return "{} - {}".format(self.movie_title, self.id)

    def get_cat_name(self):

        for key in self.genre_dict:
            if (self.genre_dict[key] ==  self.movie_genre):
                return key
                                
    def get_cat_name2(self):

        for key in self.genre_dict2:
            if (self.genre_dict2[key] ==  self.movie_genre2):
                return key
    


def add_cat_names(request):    
    return {"categories": Movie.genre_dict.keys()}
        
def add_cat_names2(request):    
    return {"categories": Movie.genre_dict2.keys()}

	
	


	
	
    
    
