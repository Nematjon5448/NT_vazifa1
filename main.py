# 1-misol

from decimal import Decimal
from random import random
import random

class DEC:
    def __set_name__(self, owner, name):
         self.name = "_" + name

    def __set__(self, instance, value: Decimal):
         if type(value) is str and value.isdecimal():
             instance.__dict__[self.name] = value
         else:
             try:
                raise ValueError("Decimal tipida kiritilmadi!!!")
             except ValueError as e:
                 print(e)

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

sanalar = []

class Valyuta:
    summa = DEC()
    def __init__(self, summa: str):
        self.summa = summa

        for i in range(31):
            sanalar.append(f"2024.12.{i}")

    def konfer(self):
        som = Decimal(self.summa) * Decimal("12000")
        return f"{som} UZS (Sana: {random.choice(sanalar)})"

d = Valyuta("99")
print(d.konfer())

# 2 - misol

from decimal import Decimal
from random import random
import random

class Dec:
    def __set_name__(self, owner, name):
         self.name = "_" + name

    def __set__(self, instance, value: Decimal):
         if type(value) is str and value.isdecimal() and value < Decimal("0"):
             instance.__dict__[self.name] = value
         else:
             try:
                raise ValueError("Decimal tipida kiritilmadi!!!")
             except ValueError as e:
                 print(e)

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

sanalar = []

class Mahsulot:
    def __init__(self, mahsulot_narxi):
        self.mahsulot_narxi = mahsulot_narxi
        for i in range(31):
            sanalar.append(f"2024.12.{i}")

    def chegirma(self):
        chegirma = random.randint(1, 50)
        chegirma = Decimal(chegirma)
        yangi_narx = Decimal(self.mahsulot_narxi) - ((Decimal(self.mahsulot_narxi) / Decimal("100")) * Decimal(chegirma))
        return (f"Mahsulot narxi: {self.mahsulot_narxi}, chegirma: {chegirma}%\n"
                f"Yangi narx: {yangi_narx} UZS (Sana: {random.choice(sanalar)})")

p = Mahsulot("200000")
print(p.chegirma())