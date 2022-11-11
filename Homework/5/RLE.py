# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
while True:
    chs = input("""
Выберите действие:
1 - Запаковать строку
2 - Распаковать строку \n""")
    if not chs.isdigit():
        print("Нужно ввести число")
    elif int(chs) not in (1, 2):
        print("Число должно быть 1 или 2")
    else:
        break
if int(chs) == 1:
    with open('input.txt', "r") as fl_input, open("output.txt", "w") as fl_output:
        st = fl_input.read()
        len_st = len(st)
        new_st = [st[0]]
        n = 1
        for i in range(1, len_st):
            if st[i] == st[i - 1]:
                n += 1
                if i == len_st - 1:
                    new_st.append(str(n))
            else:
                new_st.extend([str(n), st[i]])
                n = 1
                if i == len_st - 1:
                    new_st.append(str(n))
            final_output = ''.join(new_st)
        print(final_output, file=fl_output)
        print(f"Строка\n{st}\nзапакована в\n{final_output}")
        print(f'Длина исходной строки: {len_st}', f'Длина результата: {len(final_output)}', f'Сжатие: '
                                                                      f'{1 - len(final_output) / len_st:.2%}', sep='\n')
else:
    with open('output.txt', "r") as fl_input:
        a = fl_input.read()
        st = list(a.removesuffix("\n"))
        lst_symb = []
        for i in range(len(st)):
            if not st[i].isdigit():
                lst_symb.append(st[i])
                st[i] = " "
        st_final = ''.join(st).split()
        print(f"Строка\n{a}распакована в\n{''.join([y * int(i) for i, y in zip(st_final, lst_symb)])}")
