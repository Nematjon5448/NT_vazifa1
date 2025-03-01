from django.shortcuts import render, redirect
from .models import Kurs, Dars, Comment
from .forms import CommentForm, LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def asosiy_sahifa(request):
    kurs = Kurs.objects.all()
    dars = Dars.objects.all()

    context = {
        'kurs': kurs,
        'dars': dars
    }

    return render(request, 'asosiy_sahifa.html', context)

def kurs_batafsil(request, kurs_id):
    kurs = Kurs.objects.get(pk=kurs_id)
    dars = Dars.objects.filter(kurs_id=kurs_id)

    context = {
        'kurs': kurs,
        'dars': dars,
    }

    return render(request, 'kurs_batafsil.html', context)

def dars_batafsil(request, dars_id):
    dars = Dars.objects.get(pk=dars_id)

    context = {
        'dars': dars,
        'form': CommentForm(),
        'comments': Comment.objects.filter(dars=dars)
    }
    return render(request, 'dars_batafsil.html', context)

def comment_saqlash(request, dars_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            if form.is_valid():
                dars = Dars.objects.get(pk=dars_id)
                comment = form.save(commit=False)
                comment.dars = dars
                comment.foydalanuvchi = request.user
                comment.save()
                messages.success(request, "Komment muvaffaqiyatli qo'shildi!!!")
            messages.error(request, "Nimadir xato ketdi!!!")
    else:
        messages.warning(request, "Iltimos avval ro'yxatdan o'tin!!!")
    return redirect('dars_batafsil', dars_id)

def comment_yangilash(request, dars_id, comment_id):
    dars = Dars.objects.get(pk=dars_id)
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(data=request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('dars_batafsil', dars_id)

    form = CommentForm(instance=comment)
    context = {
        "form": form,
        "dars": dars,
        'comment': comment
    }
    return render(request, 'dars_batafsil.html', context)

def comment_ochirish(request, dars_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.user == comment.foydalanuvchi or request.user.is_superuser:
        messages.success(request, "Komment muvaffaqiyatli o'chirildi!!!")
        comment.delete()
        return redirect('dars_batafsil', dars_id)
    else:
        messages.warning(request, "Sizda bunday huquq yo'q!!!")
        return redirect('dars_batafsil', dars_id)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Xush kelibsiz {user.username}")
            return redirect('asosiy_sahifa')
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, 'auth/login.html', context)

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account muvaffaqiyatli ochildi')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)

def user_logout(request):
    logout(request)
    messages.warning(request, 'Siz accountdan chiqdingiz!!!')
    return redirect('login')