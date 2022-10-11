# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

x = int(input("Введите номер координатной четверти "))
txt = 'Диапазон возможных координат: Х ∈ {}, У ∈ {}'
pos = '0...∞'
neg = '-∞...0'
if 0 < x > 4:
    print("Такой координатной четверти не существует")
else:
    if x == 1:
        print(txt.format(pos, pos))
    elif x == 2:
        print(txt.format(neg, pos))
    elif x == 3:
        print(txt.format(neg, neg))
    else:
        print(txt.format(pos, neg))
