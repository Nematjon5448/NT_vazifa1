# 1 - vazifa

# from collections import namedtuple
#
# students = [
#     ("Nematjon", 22, "major"),
#     ("Saidazimxon", 21, "major")
# ]
#
# Students = namedtuple("Person", ["name", "age", "major"])
#
# for student in students:
#     student1 = Students(*student)
#     print(f"Name: {student1.name}. Age: {student1.age}. Major: {student1.major}")

# 2 - vazifa

# from collections import namedtuple
#
# mahsulotlar = [
#     ("asal", 180000, "1 kg"),
#     ("shakar", 16000,"1 kg"),
#     ("un", 20000, "2 kg")
# ]
#
# Mahsulot = namedtuple("Mahsulot", ["product_name", "price", "quantity"])
#
# for mahsulot in mahsulotlar:
#     mahsulot1 = Mahsulot(*mahsulot)
#     print(f"Mahsulot nomi: {mahsulot1.product_name}, Narxi: {mahsulot1.price}, Miqdori: {mahsulot1.quantity}")

# 3 - vazifa

# from collections import namedtuple
#
# shaharlar = [
#     ("Toshkeny", "O'zbekiston", 3075000),
#     ("Moskva", "Rassiya", 144000000),
#     ("Anqara", "Turkiya", 5600000)
# ]
#
# Shahar = namedtuple("Shahar", ["city_name", "country", "population"])
# aholi = []
#
# for shahar in shaharlar:
#     shahar1 = Shahar(*shahar)
#     aholi.append(shahar1.population)
#
# max_aholi = max(aholi)
#
# for shahar in shaharlar:
#     shahar1 = Shahar(*shahar)
#     if shahar1.population == max_aholi:
#         print(f"Shahar: {shahar1.city_name}, Davlat: {shahar1.country}, Aholi soni: {shahar1.population}")

# 4 - vazifa

# from collections import namedtuple
#
# mashinalar = [
#     ("Germaniya", "BMW M5", 2022),
#     ("O'zbekiston", "Gentra", 2024),
#     ("Yaponiya", "Toyota Camry", 2021)
# ]
#
# Mashinalar = namedtuple("Mashinalar", ["make", "model", "year"])
# yili = []
#
# for mashina in mashinalar:
#     mashina1 = Mashinalar(*mashina)
#     yili.append(mashina1.year)
#
# new_car = max(yili)
#
# for mashina in mashinalar:
#     mashina1 = Mashinalar(*mashina)
#     if mashina1.year == new_car:
#         print(f"Davlati: {mashina1.make}, Modeli: {mashina1.model}, Yili: {mashina1.year}")

# 5 - vazifa

# def salom():
#     def hayr():
#         print("Hayr")
#     hayr()
#
# salom()

# 6 - vazifa

# def ism(ism):
#     def salom():
#         print(f"Salom {ism}")
#     salom()
#
# ism("Nematjon")

# 7 - vazifa

# def son1(son):
#     def son2():
#         return son + 5
#     return son2()
#
# print(son1(17))

# 8 - vazifa

# def raqam():
#     son = 0
#     def counter():
#         nonlocal son
#         son += 1
#         return son
#     return counter
#
# c = raqam()
#
# print(c())
# print(c())
# print(c())

# 9 - vazifa

# def raqam(son):
#     def kvadrat():
#         return son ** 2
#     return kvadrat()
#
# print(raqam(5))

# 10 - vazifa

# def ismlar():
#     ismlar = []
#     def ismqoshish(ism):
#         nonlocal ismlar
#         ismlar.append(ism)
#         return ismlar
#     return ismqoshish
#
# ism = ismlar()
#
# print(ism("Nematjon"))
# print(ism("Saidazimxon"))
# print(ism("Shoxrux"))

# 11 - vazifa

# def chegirma(foiz):
#     def narx(summa):
#         f = summa / 100 * foiz
#         return summa - f
#     return narx
#
# narx = chegirma(16)
# print(narx(250000))

# 12 - vazifa

# def mahsulot():
#     mahsulotlar = []
#     def mahsulotqoshish(mahsulot):
#         nonlocal mahsulotlar
#         mahsulotlar.append(mahsulot)
#         return mahsulotlar
#     return mahsulotqoshish
#
# mahsulot1 = mahsulot()
#
# print(mahsulot1("Olma"))
# print(mahsulot1("Anor"))
# print(mahsulot1("Uzum"))

# 13 - vazifa

# def matn():
#     matn1 = ""
#     def matn_qoshish(matn: str):
#         nonlocal matn1
#         matn1 += matn
#         return matn1
#     return matn_qoshish
#
# m = matn()
# print(m("Salom"))
# print(m(" Dunyo"))
# print(m(" Hello World"))

# 14 - vazifa

# def raqam():
#     son = -1
#     def count():
#         nonlocal son
#         son += 2
#         return son
#     return count
#
# toq_son = raqam()
#
# print(toq_son())
# print(toq_son())
# print(toq_son())
# print(toq_son())

# 15 - vazifa

# def son1(son: int):
#     def daraja1(daraja: int):
#         return son ** daraja
#     return daraja1
#
# son = son1(3)
# print(son(5))
# print(son(3))

# 16 - vazifa

# def matn1(matn: str):
#     def teskari_matn():
#         return matn[::-1]
#     return teskari_matn()
#
# print(matn1("Tashkent"))
# print(matn1("Najot Ta'lim"))
