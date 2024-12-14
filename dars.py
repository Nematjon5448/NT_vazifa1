# 1 - vazifa

# from collections import namedtuple
#
# Sportchi = namedtuple("Sportchi", ["ism", "sport_turi", "yutuqlari"])
#
# sportchilar = [
#     ("Nematjon", "Basketbol", 12),
#     ("Abdulaziz", "Futbol", 20),
#     ("Fayzullo", "Shaxmat", 5)
# ]
#
# yutuqlar = []
#
# for sportchi in sportchilar:
#     sport = Sportchi(*sportchi)
#     yutuqlar.append(sport.yutuqlari)
#
# eng_zori = max(yutuqlar)
#
# for sportchi in sportchilar:
#     sport = Sportchi(*sportchi)
#     if eng_zori == sport.yutuqlari:
#         print(f"Ismi: {sport.ism}, Sport turi: {sport.sport_turi}, Yutuqlari: {sport.yutuqlari}")

# 2 - vazifa

# ishchilar_yoshi = [20, 54, 18, 40, 33, 22]
# orta_hisob = sum(ishchilar_yoshi) / len(ishchilar_yoshi)
# print(orta_hisob)

# 3 - vazifa

# from typing import Iterable
#
# sonlar = range(1, 10)
#
# class CustomIterator:
#     def __init__(self, sonlar: Iterable):
#         self.sonlar = sonlar
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index >= len(self.sonlar):
#             return print("Element qolmadi!")
#         return sonlar[self.index] ** 2
#
# son = CustomIterator(sonlar)
# print(next(son))
# print(next(son))
# print(next(son))
# print(next(son))

# 4 - vazifa

# matn = "Najot Ta'lim markazi"
# matndagi_unli_harflar = ""
# for i in matn:
#     if i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u" :
#         matndagi_unli_harflar += f"{i} "
#
# print(matndagi_unli_harflar)

# 5 - vazifa

# def generator_number():
#     for i in range(1, 100):
#         yield i
#
# for i in generator_number():
#     print(i)

# 6 - vazifa

# def matn(matn):
#     def matn_uzunligi():
#         return len(matn)
#     return matn_uzunligi()
#
# print(matn("Najot Ta'lim)"))