# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import sample, randint

lst = sample(range(30), randint(4, 12))
print('Сгенерирован список чисел', *lst)
suma = 0
odd_lst = []
for i in range(1, len(lst), 2):
    suma += lst[i]
    odd_lst.append(str(lst[i]))
print(f'Сумма элементов на нечетных позициях {" + ".join(odd_lst)} = {suma}')
