from django.shortcuts import render
#from django.http import HttpResponse
from books.models import Author#, Book
# Create your views here.
def authors_list(request):
    a = Author.objects.all()
    return render(request, 'authors.html', {'authors': a},)
