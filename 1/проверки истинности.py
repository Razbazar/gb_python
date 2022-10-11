# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

io = (0, 1)
lst = ['ложно', 'истинно']
for x in io:
    for y in io:
        for z in io:
            a = not (x or y or z)
            b = (not x) and (not y) and (not z)
            t = a == b
            print(f"Для X = {x}, Y = {y}, Z = {z} утверждение {lst[t]}")