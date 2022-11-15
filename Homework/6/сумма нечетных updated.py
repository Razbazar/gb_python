# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import sample, randint

lst = sample(range(30), randint(4, 12))
print('Сгенерирован список чисел', *lst)
odd_lst = list(filter(lambda x: lst.index(x) % 2, lst))
print(f'Сумма элементов на нечетных позициях {odd_lst} = {sum(odd_lst)}')

