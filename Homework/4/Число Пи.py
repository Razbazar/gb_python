# Вычислить число Пи c заданной точностью d


def pi_digit(n):
    p = 0
    for i in range(n):
        p += 1 / pow(16, i) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))
    return p


print(pi_digit(100))
d = str(float(input("Введите точность \n"))).split('.')
print(d)
# print(round(pi_digit(100), d))


