# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input("Введите х координату "))
y = int(input("Введите у координату "))
str1 = "точка ({}, {}) лежит на оси Y и принадлежит {} и {} координатным осям"
str2 = "точка ({}, {}) принадлежит {} координатной плоскости"

if not x and not y:
    print("точка находится в центре координат")
else:
    if x == 0:
        print(str1.format(x, y, '1', '2') if y > 0 else print(str1.format(x, y, '3', '4')))
    elif y == 0:
        print(str1.format(x, y, '1', '4') if x > 0 else print(str1.format(x, y, '2', '3')))
    elif x > 0:
        print(str2.format(x, y, '1') if y > 0 else str2.format(x, y, '4'))
    else:
        print(str2.format(x, y, '2') if y > 0 else str2.format(x, y, '3'))
