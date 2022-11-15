# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import sample, randint

lst = sample(range(1, 10), randint(4, 7))
print('Сгенерирован список чисел', *lst)
prod_lst = list(map(lambda x: lst[x] * lst[-(x+1)], range((len(lst) // 2) + (len(lst) % 2))))
print('Итоговый список произведений пар:', prod_lst)
