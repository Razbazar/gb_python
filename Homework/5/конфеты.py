# Создайте программу для игры с конфетами человек против человека.
from random import choice, randint


def check(vibor, limit=28, game=False):
    global stack
    if not vibor.isdigit():
        print("Ввести нужно число. Повторите")
        return True
    elif int(vibor) not in range(1, limit + 1):
        if not game:
            limit = stack
        print(f"Число должно быть в пределах от 1 до {limit}. Повторите")
        return True
    elif game and int(vibor) > stack:
        print(f"Такого количества конфет на столе нет. На столе осталось {stack} конфет")
        return True
    else:
        return False


def bot(limit):
    global stack
    if limit > stack:
        limit = stack
    v = randint(1, limit)
    stack -= v
    return v


stack = 2021
while True:
    chs = input("Выберите режим игры. 1 - с ботом, 2 - с человеком ")
    if not check(chs, limit=2):
        break
x = choice([0, 1])
if int(chs) == 2:
    print("Игра с человеком")
    while stack > 0:
        if x == 0:
            x = 1
        else:
            x = 0
        while True:
            k = input(f"{x+1}-й игрок забирает конфеты: ")
            if not check(k, game=True):
                break
        stack -= int(k)
        print(f"Осталось {stack} конфет" if stack != 0 else "Конфет не осталось")
    print(f'{x+1}-й игрок победил')
else:
    print("Игра с ботом")
    while stack > 0:
        if x == 0:
            print(f"Ход бота. Он взял {bot(28)}. Осталось {stack} конфет")
            x = 1
        else:
            while True:
                k = input("Человек забирает конфеты: ")
                if not check(k, game=True):
                    break
            stack -= int(k)
            x = 0
            print(f"Осталось {stack} конфет" if stack != 0 else "Конфет не осталось")
    print(f'{("Человек", "Бот")[x]} победил')
