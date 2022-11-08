# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k

from random import randint

upper_dig = [8304, 185, *range(178, 180), *range(8308, 8314)]
k = int(input("Введите степень \n"))
lst = []
for i in range(k+1, 0, -1):
    chln = randint(0, 3)
    if chln == 0:
        continue
    sign = ""
    iks = 'X'
    if chln > 0:
        sign = "+"
    if chln == 1:
        chln = ''
    stepen = chr(upper_dig[i - 1])
    if i <= 2:
        stepen = ""
    if i == 1:
        iks = ""
    arg = iks + stepen
    lst.append(sign + str(chln) + arg)
with open("output.txt", mode="w", encoding="utf-8") as fl:
    print(''.join(lst).lstrip('+')+'=0', file=fl)
