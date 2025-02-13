from django.shortcuts import render
from .models import Book, Author, Review

def index_1(request):
    book = Book.objects.all()

    context = {
        'book': book,
    }

    return render(request, 'index_1.html', context)

def index_2(request):
    author = Author.objects.all()

    context = {
        'author': author,
    }

    return render(request, 'index_2.html', context)

def index_3(request):
    review = Review.objects.all()
    book = Book.objects.all()

    context = {
        'review': review,
        'book': book
    }

    return render(request, 'index_3.html', context)