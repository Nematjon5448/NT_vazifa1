from django.shortcuts import render, redirect
from .models import Brand, Car
from .forms import BrandForm, CarForm

# Create your views here.

def asosiy_sahifa(request):
    brand = Brand.objects.all()
    car = Car.objects.all()

    context = {
        'brand': brand,
        'car': car
    }

    return render(request, 'asosiy_sahifa.html', context)

def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(data=request.POST)
        if form.is_valid():
            brand = Brand.objects.create(**form.cleaned_data)
            return asosiy_sahifa(request)
    context = {
        'form': BrandForm()
    }
    return render(request, 'add_brand.html', context)

def add_car(request):
    if request.method == 'POST':
        form = CarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            car = Car.objects.create(**form.cleaned_data)
            return asosiy_sahifa(request)
    context = {
        'form': CarForm()
    }
    return render(request, 'add_car.html', context)

def update_brand(request, brand_id):
    brand = Brand.objects.get(pk=brand_id)

    if request.method == 'POST':
        form = BrandForm(data=request.POST)
        if form.is_valid():
            brand.nomi = form.cleaned_data.get('nomi')
            brand.davlati = form.cleaned_data.get('davlati')
            brand.save()
            return redirect('brand_detail', brand.pk)
    form = BrandForm(initial={
        'nomi': brand.nomi,
        "davlati": brand.davlati
    })
    context = {
        "form": form
    }
    return render(request, 'add_brand.html', context)

def brand_detail(request, brand_id):
    brand = Brand.objects.filter(id=brand_id)
    car = Car.objects.filter(brand_id=brand_id)

    context = {
        'brand': brand,
        'car': car
    }
    return render(request, 'brand_detail.html', context)

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    brand = Brand.objects.all()

    context = {
        'car': car,
        'brand': brand
    }
    return render(request, 'car_detail.html', context)

def update_car(request, car_id):
    car = Car.objects.get(pk=car_id)

    if request.method == 'POST':
        form = CarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            car.model = form.cleaned_data.get('model')
            car.ot_kuchi = form.cleaned_data.get('ot_kuchi')
            car.rangi = form.cleaned_data.get('rangi')
            car.narxi = form.cleaned_data.get('narxi')
            car.brand = form.cleaned_data.get('brand')
            if form.cleaned_data.get('rasmi'):
                car.rasmi = form.cleaned_data.get('rasmi')
            car.save()
            return redirect('car_detail', car.pk)
    form = CarForm(initial={
        'model': car.model,
        "ot_kuchi": car.ot_kuchi,
        "rangi": car.rangi,
        "narxi": car.narxi,
        "brand": car.brand,
    })
    context = {
        "form": form
    }
    return render(request, 'add_car.html', context)

