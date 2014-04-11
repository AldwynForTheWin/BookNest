from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from booksys.models import Book

def index(request):
	latest_book_list = Book.objects.order_by('title')
	return render(request, 'booksys/index.html', {'latest_book_list': latest_book_list})

def detail(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	return render(request, 'booksys/detail.html', {'book': book})

def results(request, book_id):
	return HttpResponse("You're looking at the results of %s." % book_id)