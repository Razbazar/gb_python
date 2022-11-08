# сформировать файл, содержащий сумму многочленов.

from sympy import sympify


def replace_func(lst):
    global stepen_dict
    for j in range(len(lst)):
        lst[j] = lst[j].lstrip("*")
        if ord(lst[j][-1]) in stepen_dict:
            lst[j] = lst[j].replace(lst[j][-1], '**' + str(stepen_dict[ord(lst[j][-1])]))
    return lst


stepen_dict = dict(zip([8304, 185, *range(178, 180), *range(8308, 8314)], range(10)))
with open("1.txt", "r", encoding="utf-8") as fl_one, open("2.txt", "r", encoding="utf-8") as fl_two, \
        open('3.txt', 'w', encoding="utf-8") as fl_three:
    first = sympify(''.join(replace_func(fl_one.read().removesuffix(' = 0').replace("x", "*x").split())))
    second = sympify(''.join(replace_func(fl_two.read().removesuffix(' = 0').replace("x", "*x").split())))
    final = str(first + second).replace('*', '').split()
    for i in range(len(final)):
        if final[i][-1] in map(str, list(stepen_dict.values())) and "x" in final[i]:
            final[i] = final[i].replace(final[i][-1], chr(list(stepen_dict.keys())[list(stepen_dict.values()).index(int(final[i][-1]))]))
    print(" ".join(final)+" = 0", file=fl_three)

