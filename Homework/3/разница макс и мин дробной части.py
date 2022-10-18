# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import randint, random

lst_dig = []


def find_decimal(x):
    global lst_dig
    return round(lst_dig[x] - int(lst_dig[x]), 2)


for i in range(randint(2, 10)):
    lst_dig.append(round(random() * 100, 2))
print('Сгенерирован список вещественных чисел:', *lst_dig)
max_decimal = find_decimal(0)
min_decimal = find_decimal(1)
for i in range(len(lst_dig)):
    tmp = find_decimal(i)
    if tmp > max_decimal:
        max_decimal = tmp
    if tmp < min_decimal:
        min_decimal = tmp

print(f'Разница между максимальной дробной части {max_decimal} и минимальной {min_decimal} равна {round(max_decimal - min_decimal, 2)}')
