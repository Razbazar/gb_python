from random import uniform

x = str(round(uniform(0, 20), 4))
summa = 0
for i in x:
    if i.isdigit():
        summa += int(i)
print(f"Сумма цифр числа {x} = {summa}")
