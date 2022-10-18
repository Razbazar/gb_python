n = int(input("Введите число N "))
summa = 0
lst = []


def formula(x):
    return round(pow((1+1/x), x), 2)


for i in range(1, n + 1):
    el = formula(i)
    summa += el
    lst.append(el)

print(f"Список последовательности: {lst}", f"сумма его элементов: {summa:.2f}", sep="\n")

x = 494
"tire"
