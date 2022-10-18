# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import sample, randint
from math import ceil

lst = sample(range(1, 10), randint(4, 7))
print('Сгенерирован список чисел', *lst)
prod_lst = []
for i in range(ceil((len(lst) / 2))):
    prod_lst.append(lst[i] * lst[-(i+1)])
    print(f'{str(lst[i]) + " * " + str(lst[-(i+1)])} = {lst[i] * lst[-(i+1)]}')

print('Итоговый список произведений пар:', *prod_lst)
