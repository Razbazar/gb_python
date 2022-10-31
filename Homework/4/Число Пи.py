# Вычислить число Пи c заданной точностью d
def pi_digit(n):
    p = 0
    for i in range(n):
        p += 1 / pow(16, i) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))
    return p


print(pi_digit(1000))
d = input("Введите точность \n")
print(len(d[2:]))
print(round(pi_digit(100), len(d[2:])))