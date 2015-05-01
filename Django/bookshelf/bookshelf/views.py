from django.shortcuts import render
#from django.http import HttpResponse
from books.models import Author, Book
# Create your views here.
def authors_list(request):
    a = Author.objects.all()
    return render(request, 'authors.html', {'authors': a},)

def authors_detail(request, num=None):
    a = Author.objects.get(id = num)
    b = Book.objects.filter(authors = a)


    return render(request, 'author_detail.html',{'authors': a, 'books': b},)
