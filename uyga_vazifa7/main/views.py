from django.shortcuts import render, redirect
from .forms import BookForm, CommentForm
from .models import Category, Book, Comment


# Create your views here.

def asosiy_sahifa(request):
    category = Category.objects.all()
    book = Book.objects.all()

    context = {
        'category': category,
        'book': book
    }

    return render(request, 'asosiy_sahifa.html', context)

def kitoblar(request, category_id):
    category = Category.objects.filter(pk=category_id)
    book = Book.objects.filter(category_id=category_id)

    context = {
        'category': category,
        'book': book
    }

    return render(request, 'kitoblar.html', context)

def kitob_haqida(request, book_id):
    book = Book.objects.get(pk=book_id)

    context = {
        'book': book,
        'form': CommentForm(),
        'comments': Comment.objects.filter(book=book)
    }

    return render(request, 'kitob_haqida.html', context)

def kitob_qoshish(request):
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = Book.objects.create(**form.cleaned_data)
            return asosiy_sahifa(request)

    context = {
        'form': BookForm()
    }
    return render(request, 'kitob_qoshish.html', context)

def kitob_yangilash(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.title = form.cleaned_data.get('title')
            book.category = form.cleaned_data.get('category')
            book.publication_date = form.cleaned_data.get('publication_date')
            book.isbn = form.cleaned_data.get('isbn')
            book.genre = form.cleaned_data.get('genre')
            book.summary = form.cleaned_data.get('summary')
            book.views = form.cleaned_data.get('views')
            book.save()
            return redirect('kitob_haqida', book.pk)

    form = BookForm(initial={
        'title': book.title,
        'category': book.category,
        'publication_date': book.publication_date.strftime('%Y-%m-%d') if book.publication_date else '',
        'isbn': book.isbn,
        'genre': book.genre,
        'summary': book.summary,
        'views': book.views
    })
    context = {
        'form': form
    }
    return render(request, 'kitob_qoshish.html', context)

def kitob_ochirish(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('asosiy_sahifa')
    return render(request, 'confirm_delete.html', {'book': book})

def save_comment(request, book_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            if form.is_valid():
                book = Book.objects.get(pk=book_id)
                comment = form.save(commit=False)
                comment.book = book
                comment.user = request.user
                comment.save()
    return redirect('kitob_haqida', book_id)

