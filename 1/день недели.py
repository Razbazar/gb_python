# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

labor = list(range(1, 6))
x = int(input("Введите число "))
if 0 < x > 7:
    print("Такого дня недели нет")
else:
    print(f"{x}-й день недели рабочий" if x in labor else f"{x}-й день недели выходной")
