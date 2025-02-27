from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Brand, Rang, Car, Comment
from .forms import CommentForm
from django.contrib.auth import login, authenticate, logout

def asosiy_sahifa(request):
    brandlar = Brand.objects.all()
    ranglar = Rang.objects.all()

    context = {
        'brandlar': brandlar,
        'ranglar': ranglar,
    }

    return render(request, 'asosiy_sahifa.html', context)

def brand_boyicha(request, brand_id):
    brand = Brand.objects.get(pk=brand_id)
    mashina = Car.objects.filter(brand_id=brand_id)
    ranglar = Rang.objects.all()
    brandlar = Brand.objects.all()

    context = {
        'brand': brand,
        'mashina': mashina,
        'ranglar': ranglar,
        'brandlar': brandlar
    }

    return render(request, 'asosiy_sahifa.html', context)

def rang_boyicha(request, rang_id):
    rang = Rang.objects.get(pk=rang_id)
    mashinalar = Car.objects.filter(rang_id=rang_id)
    ranglar = Rang.objects.all()
    brandlar = Brand.objects.all()

    context = {
        'rang': rang,
        'mashinalar': mashinalar,
        'ranglar': ranglar,
        'brandlar': brandlar
    }

    return render(request, 'asosiy_sahifa.html', context)

def mashina_batafsil(request, car_id):
    mashina = Car.objects.get(pk=car_id)

    context = {
        'mashina': mashina,
        'form': CommentForm(),
        'commentlar': Comment.objects.filter(mashina=mashina)
    }
    return render(request, 'mashina_batafsil.html', context)

def comment_saqlash(request, car_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            if form.is_valid():
                mashina = Car.objects.get(pk=car_id)
                comment = form.save(commit=False)
                comment.foydalanuvchi = request.user
                comment.mashina = mashina
                comment.save()

    return redirect('mashina_batafsil', car_id)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, f"Xush kelibsiz {user.username}")
        return redirect('asosiy_sahifa')
    return render(request, 'auth/login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            messages.success(request, 'Account muvaffaqiyatli ochildi!!!')
        return redirect('login')
    return render(request, 'auth/register.html')

def user_logout(request):
    logout(request)
    messages.warning(request, 'Siz accountdan chiqdingiz!!!')
    return redirect('login')
