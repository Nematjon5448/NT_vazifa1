from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Brand, Rang, Car, Comment
from .forms import CommentForm, CarForm
from django.contrib.auth import login, authenticate, logout

def asosiy_sahifa(request):
    return render(request, 'asosiy_sahifa.html')

class BrandBoyichaView(ListView):
    model = Car
    template_name = 'asosiy_sahifa.html'
    context_object_name = 'mashina'
    ordering = 'nomi'

    def get_queryset(self):
        brand_id = self.kwargs.get('brand_id')
        return Car.objects.filter(brand_id=brand_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        brand_id = self.kwargs.get('brand_id')
        context['brand'] = Brand.objects.get(pk=brand_id)
        return context

class RangBoyichaListView(ListView):
    model = Car
    template_name = 'asosiy_sahifa.html'
    context_object_name = 'mashinalar'

    def get_queryset(self):
        rang_id = self.kwargs.get('rang_id')
        return Car.objects.filter(rang_id=rang_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        rang_id = self.kwargs.get('rang_id')
        context['rang'] = Rang.objects.get(pk=rang_id)
        return context

class MashinaBatafsilDetailView(DetailView):
    model = Car
    context_object_name = 'mashina'
    pk_url_kwarg = 'car_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        car_id = self.kwargs.get('car_id')
        context['commentlar'] = Comment.objects.filter(mashina=car_id)
        return context

class CommentSaqlashView(View):
    def post(self, request, car_id):
        if request.user.is_authenticated:
            form = CommentForm(data=request.POST)
            if form.is_valid():
                mashina = Car.objects.get(pk=car_id)
                comment = form.save(commit=False)
                comment.foydalanuvchi = request.user
                comment.mashina = mashina
                comment.save()
                return redirect('mashina_batafsil', car_id)

    def get(self, request, car_id):
        return redirect('mashina_batafsil', car_id)

class UserLoginView(View):
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Xush kelibsiz {user.username}")
            return redirect('asosiy_sahifa')

    def get(self, request):
        return render(request, 'auth/login.html')

class UserRegisterView(View):
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                user = User.objects.create_user(username=username, email=email, password=password1)
                messages.success(request, 'Account muvaffaqiyatli ochildi!!!')
            return redirect('login')

    def get(self, request):
        return render(request, 'auth/register.html')

def user_logout(request):
    logout(request)
    messages.warning(request, 'Siz accountdan chiqdingiz!!!')
    return redirect('login')

class MashinaQoshishCreateView(CreateView):
    model = Car
    fields = '__all__'
    template_name = 'add_car.html'

    def get_success_url(self):
        return reverse_lazy('mashina_batafsil', kwargs={'car_id': self.object.pk})
