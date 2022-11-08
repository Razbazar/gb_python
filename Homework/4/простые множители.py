# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple(x):
    for i in range(2, x + 1):
        if not x % i:
            return i


n = int(input("Введите число N "))
lst = []
ch = 2
while n > 1:
    ch = simple(int(n))
    lst.append(ch)
    n /= ch

print(lst)
