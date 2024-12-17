# 1 - vazifa

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def kvadrat_son(son: int):
#     return son ** 2
#
# result = list(map(kvadrat_son, numbers))
# print(result)

# 2 - vazifa

# def katta_harf(harf: str):
#     return harf.isupper()
#
# harflar = ["A", "a", "B", "b", "C", "c", "D", "d"]
# katta_harflar = list(filter(katta_harf, harflar))
# print(katta_harflar)

# 3 - vazifa

# def region_number(number: str):
#     if number.startswith("+998"):
#         return number + " Uzb"
#     elif number.startswith("+7"):
#         return number + " Rus"
#     elif number.startswith("+1"):
#         return number + " USA"
#
# phone_numbers = ["+998991234567", "+79454874459", "+14385001031"]
# result = list(map(region_number, phone_numbers))
# print(result)

# 4 - vazifa

# def cap(name: str):
#     return name.capitalize()
#
# names = ['alfred', 'tabitha', 'william', 'arla']
# ismlar = list(map(cap, names))
# print(ismlar)

# 5 - vazifa

# def katta_son(son: int):
#     return son > 75
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# katta_sonlar = list(filter(katta_son, scores))
# print(katta_sonlar)

# 6 - vazifa

# def palindrom(word: str):
#     return word.lower() == word[::-1].lower()
#
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# res = list(filter(palindrom, words))
# print(res)

# 7 - vazifa

# def lens(word: str):
#     return len(word)
#
# mevalar = ["Olma", "Anor", "Banan", "Tarvuz", "Nok"]
# res = list(map(lens, mevalar))
# print(res)

# 8 - vazifa

# def merge(meva1: str, meva2: str):
#     return meva1 + meva2
#
# mevalar1 = ["apple", "banana", "cherry"]
# mevalar2 = ["orange", "lemon", "pineapple"]
#
# res = list(map(merge, mevalar1, mevalar2))
# print(res)

# 9 - vazifa

# def merge(ism1: str, ism2: str):
#     return ism1 + ism2
#
# ismlar1 = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# ismlar2 = ["Sobir", "Bakir", "Jalil", "Toxir"]
#
# res = list(map(merge, ismlar1, ismlar2))
# print(res)

# 10 - vazifa

# def takror(mevalar: list, meva: str):
#     return mevalar.count(meva)
#
# fruits = ["Olma", "Anor", "Olma", "Gilos", "Banan", "Olma"]
# print(takror(fruits, 'Olma'))

# 11 - vazifa

# def sonlar(num1: int):
#     nums2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#     return num1 in nums2
#
# nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# res = list(filter(sonlar, nums1))
# print(res)

# 12 - vazifa

# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin',
#                          'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby',
#                          'Rust', 'Mojo', 'Swift', 'Php']
#
# def toq_tartib(word: str):
#     return programming_languages.index(word) % 2 == 0
#
# res = list(filter(toq_tartib, programming_languages))
# print(res)

# 13 - vazifa

# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin',
#                          'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby',
#                          'Rust', 'Mojo', 'Swift', 'Php']
#
# def toq_tartib(word: str):
#     return programming_languages.index(word) >= programming_languages.index("Basic")
#
# res = list(filter(toq_tartib, programming_languages))
# print(res)

# 14 - vazifa

# from collections import namedtuple
#
# talabalar = [
#     ("Nematjon", "FN28", 90),
#     ("Abdulaziz", "FN28", 85),
#     ("Shavkat", "FN28", 60),
#     ("Abdullo", "FN28", 95),
#     ("Ziyodullo", "FN28", 70)
# ]
#
# Student = namedtuple("Student", ["ism", "guruh", "baho"])
# baholar = []
#
# for talaba in talabalar:
#     talaba1 = Student(*talaba)
#     baholar.append(talaba1.baho)
#
# max_baho = max(baholar)
#
# for talaba in talabalar:
#     talaba1 = Student(*talaba)
#     if talaba1.baho == max_baho:
#        print(f"Ismi: {talaba1.ism}, Guruhi: {talaba1.guruh}, Baho: {talaba1.baho}")

# 15 - vazifa

# def kvadrat_generator():
#     for i in range(1, 21):
#         yield i ** 2
#
# for i in kvadrat_generator():
#     print(i)

# 16 - vazifa

# def text(matn: str):
#     def len_text():
#         return len(matn)
#     return len_text()
#
# print(text("Najot Ta'lim"))

# 17 - vazifa

# def name(ism: str):
#     def salom():
#         return f"Salom {ism}"
#     return salom()
#
# print(name("Nematjon"))