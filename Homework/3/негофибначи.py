# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input("Введите число: "))
lst = []
for i in range(k + 1):
    if i == 0:
        lst.append(0)
    elif i == 1:
        lst.append(1)
    else:
        lst.append(lst[i - 2] - lst[i - 1])
negofibo_list = list(reversed(lst))
negofibo_list.extend(list(map(lambda x: (x, -x)[x < 0], lst[1:])))
print(negofibo_list)
