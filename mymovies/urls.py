from django.conf import settings
from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^allmovies/', views.allmovies, name='allmovies'),
    url(r'^homepage/', views.homepage, name='homepage'),
	url(r'^$', views.homepage, name='homepage'),
	url(r'^questionnairepage/', views.questionnairepage, name='questionnairepage'),
	url(r'^soundtracks/', views.soundtracks, name='soundtracks'),
	url(r'^feedback/', views.feedback, name='feedback'),
	url(r'^movie/(?P<movie_title>.+)/', views.movie_page, name='movie'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

 