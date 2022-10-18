# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

dig = int(input("Введите любое целое число "))
binary_lst = []
while dig != 0:
    binary_lst.append(str(dig - 2 * (dig // 2)))
    dig = dig // 2
print("Двоичное представление этого числа:", "".join(reversed(binary_lst)))
