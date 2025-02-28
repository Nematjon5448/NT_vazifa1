from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from .models import Brand, Rang, Car, Comment
from .forms import CommentForm, SendEmail, CarForm
from django.contrib.auth import login, authenticate, logout

def asosiy_sahifa(request):
    return render(request, 'asosiy_sahifa.html')

def brand_boyicha(request, brand_id):
    brand = Brand.objects.get(pk=brand_id)
    mashina = Car.objects.filter(brand_id=brand_id)

    context = {
        'brand': brand,
        'mashina': mashina
    }

    return render(request, 'asosiy_sahifa.html', context)

def rang_boyicha(request, rang_id):
    rang = Rang.objects.get(pk=rang_id)
    mashinalar = Car.objects.filter(rang_id=rang_id)

    context = {
        'rang': rang,
        'mashinalar': mashinalar
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

def habar_yuborish(request):
    if request.method == 'POST':
        form = SendEmail(data=request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            for user in User.objects.all():
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email]
                )
        messages.success(request, "Habar yuborildi!")
        return redirect('asosiy_sahifa')
    else:
        form = SendEmail()
    context = {
        'form': form
    }
    return render(request, 'habar_yuborish.html', context)

def mashina_qoshish(request):
    if request.method == 'POST':
        form = CarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            car = Car.objects.create(**form.cleaned_data)
            for user in User.objects.all():
                send_mail(
                    subject="Mashina qo'shildi",
                    message=f"{car.nomi} mashinasi joylandi",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email]
                )
            messages.success(request, "Habar yuborildi!")
            return redirect('asosiy_sahifa')
    context = {
        'form': CarForm()
    }
    return render(request, 'add_car.html', context)
