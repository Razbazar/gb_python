from random import randint
n = int(input("Введите число N "))
prod = 1
lst = [randint(-n, n) for _ in range(n)]
print(lst)
while True:
    x = map(int, input("Введите позиции, которые необходимо перемножить через пробел ").split())
    try:
        for i in x:
            prod *= lst[i]
    except IndexError:
        print("Введённые позиции выходят за пределы списка. Попробуйте еще раз")
    else:
        print(f"Произведение выбранных позиций = {prod}")
        break
