from django.conf.urls import patterns, url
from booksys import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<book_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<book_id>\d+)/results/$', views.results, name='results'),
)