from django.shortcuts import render
import random

def asosiy(request):
    return render(request, 'asosiy.html')

def index_1(request):
    mevalar = ["Olma", "Banan", "Shaftoli", "Gilos"]
    context = {
        "mevalar": mevalar
    }
    return render(request, 'index_1.html', context)

def index_2(request):
    ism = 'Ali'
    yosh = 25
    kasb = 'Dasturchi'

    shaxs = {
        "ism": ism,
        "yosh": yosh,
        "kasb": kasb
    }
    return render(request, 'index_2.html', shaxs)

def index_3(request):
    talabalar = [
        {"ism": "Ali", "ball": 85},
        {"ism": "Vali", "ball": 60},
        {"ism": "Salim", "ball": 90}
    ]

    context = {
        'talabalar': talabalar
    }

    return render(request, 'index_3.html', context)

def index_4(request):
    mahsulotlar = [
        {"nom": "Laptop", "narx": 1500},
        {"nom": "Telefon", "narx": 800},
        {"nom": "Sichqoncha", "narx": 30},
    ]
    context = {
        "mahsulotlar": mahsulotlar
    }
    return render(request, 'index_4.html', context)

def index_5(request):
    sonlar = [42, 10, 3, 98, 55, 1]
    sonlar.sort()
    context = {
        "sonlar": sonlar
    }
    return render(request, 'index_5.html', context)

def index_6(request):
    talabalar = [
        {"ism": "Ali", "ball": 85},
        {"ism": "Vali", "ball": 60},
        {"ism": "Salim", "ball": 90},
    ]
    return render(request, 'index_6.html')

def index_7(request):
    sonlar = [4, 8, 15, 16, 23, 42]
    summa = sum(sonlar)
    context = {
        "summa": summa
    }
    return render(request, 'index_7.html', context)

def index_8(request):
    odamlar = [
        {"ism": "Ali", "yosh": 25},
        {"ism": "Vali", "yosh": 30},
        {"ism": "Salim", "yosh": 28},
    ]
    yosh = 0
    for yoshi in odamlar:
        yosh += yoshi['yosh']
    yosh = yosh / len(odamlar)
    yosh = round(yosh)

    context = {
        'yosh': yosh
    }
    return render(request, 'index_8.html', context)

def index_9(request):
    sonlar = [5, 12, 67, 89, 34, 21]
    katta_son = max(sonlar)

    context = {
        "katta_son": katta_son
    }
    return render(request, 'index_9.html', context)

def index_10(request):
    mamlakatlar = ["O‘zbekiston", "AQSh", "Rossiya", "Xitoy"]

    context = {
        "mamlakatlar": mamlakatlar
    }
    return render(request, 'index_10.html', context)

def index_11(request):
    kitoblar = [
        {"nom": "Python Asoslari", "muallif": "Guido Van Rossum"},
        {"nom": "Django Pro", "muallif": "Adrian Holovaty"},
    ]
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'index_11.html', context)

def index_12(request):
    ishchilar = [
        {"ism": "Ali", "maosh": 1200},
        {"ism": "Vali", "maosh": 1500},
        {"ism": "Salim", "maosh": 1800},
    ]
    katta_maosh = []
    for maosh in ishchilar:
        katta_maosh.append(maosh['maosh'])
    katta_maosh = max(katta_maosh)
    context = {
        'ishchilar': ishchilar,
        'katta_maosh': katta_maosh
    }
    return render(request, 'index_12.html', context)

def index_13(request):
    lotereya_sonlari = sorted(random.sample(range(1, 100), 6))
    context = {
        'lotereya_sonlari': lotereya_sonlari
    }
    return render(request, 'index_13.html', context)

def index_14(request):
    filmlar = [
        {"nom": "Inception", "yil": 2010},
        {"nom": "Interstellar", "yil": 2014},
        {"nom": "The Dark Knight", "yil": 2008},
    ]
    filmlar_sanasi = []
    for sana in filmlar:
        filmlar_sanasi.append(sana['yil'])
    eski_film = min(filmlar_sanasi)
    yangi_film = max(filmlar_sanasi)
    return render(request, 'index_14.html')

def index_15(request):
    odamlar = ["Ali", "Muhammad", "Vali", "Olimjon"]
    eng_uzun_ism = odamlar[0]
    for ism in odamlar:
        if len(ism) > len(eng_uzun_ism):
            eng_uzun_ism = ism
    context = {
        'eng_uzun_ism': eng_uzun_ism
    }
    return render(request, 'index_15.html', context)