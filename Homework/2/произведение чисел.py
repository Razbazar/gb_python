# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

x = int(input("Введите число "))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


lst = [factorial(i) for i in range(1, x + 1)]
print(lst)
