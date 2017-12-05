from django.shortcuts import render
from .models import Movie
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from mymovies.forms import ContactForm
from django.shortcuts import render
from django.core.paginator import Paginator


        
        
        
        
def allmovies(request):
    movie_list = Movie.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(movie_list, 10)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'mymovies/allmovies.html', { 'items': items })
        

        
        
def homepage(request):    
    movies2 = Movie.objects.all()
    context = {"movies": movies2}  
    return render(request, 'mymovies/homepage.html', context)
        
def questionnairepage(request):
	if request.POST:
		print(request.POST)
		movies = Movie.objects.all()
		scores = {}
		for movie in movies:
			scores[movie.id] = 0
		for movie in movies:
			print(movie.movie_super_heroes)
			if movie.movie_super_heroes == Movie.super_heroes[request.POST["movie_super_heroes"]]:
				scores[movie.id] += 3
		print(scores)	   
	return render(request, 'mymovies/questionnairepage.html', {}) 
        
def soundtracks(request):     
    movies = Movie.objects.all()
    context = {"movies": movies}  
                
    return render(request, 'mymovies/soundtracks.html', context)
        
        
def feedback(request):
    form_class = ContactForm
    
    return render(request, 'mymovies/feedback.html', {
        'form': form_class,
    })
        
def movie_page(request, movie_title):
    print(movie_title)
    movie = get_object_or_404(Movie, pk=movie_title)

    context = {"movie": movie}
    return render(request, "mymovies/movie.html", context)

