from random import randint, seed
seed(123) # изменить для генерации нового списка
lst = list(str(randint(1, 99999999)))
print(lst)
for i in range(len(lst)):
    seed()
    rnd = randint(0, len(lst) - 1)
    lst[i], lst[rnd] = lst[rnd], lst[i]
print(lst)
