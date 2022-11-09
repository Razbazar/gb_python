def matrix_create(str_input):
    matrix = []
    n = -3
    m = 0
    for rows in range(3):
        matrix.append([])
        n += 3
        m += 3
        for cols in range(n, m):
            matrix[rows].append(str_input[cols])
    return matrix


def matrix_print(matrix_):
    txt = '''{separator}
{borders} {first} {borders}
{borders} {second} {borders}
{borders} {third} {borders}
{separator}'''
    print(txt.format(separator=('-' * 9), first=' '.join(matrix_[0]), second=' '.join(matrix_[1]),
                     third=' '.join(matrix_[2]), borders='|'))



def check(z):
    winner_streak = [[0, 1, 2], [0, 3, 6], [0, 4, 8],
                     [1, 4, 7], [2, 5, 8], [2, 4, 6],
                     [3, 4, 5], [6, 7, 8]]
    count = 0
    if string[winner_streak[z][0]] == string[winner_streak[z][1]] == string[winner_streak[z][2]] == 'X' \
            or string[winner_streak[z][0]] == string[winner_streak[z][1]] == string[winner_streak[z][2]] == 'O':
        winner_is = string[winner_streak[z][0]]
        count = 1
        return [count, winner_is]
    else:
        return [count]


string = ' ' * 9
matrix_print(matrix_create(string))
turn = 'O'
winner = ''
while True:
    if winner != '':
        print(winner, 'победили')
        break
    if string.count(' ') == 0:
        print('Ничья')
        break
    coordinates = input('Введите координаты: ').replace(" ", "")
    if not coordinates.isdigit():
        print('Можно вводить только цифры!')
        continue
    if len(coordinates) != 2:
        print('Цифр в координатах должно быть две!')
        continue
    x = int(coordinates[0]) - 1
    y = int(coordinates[1]) - 1
    if int(coordinates[0]) not in range(1, 4) or int(coordinates[1]) not in range(1, 4):
        print('Координаты должны быть в диапазоне от 1 до 3!')
        continue
    if matrix_create(string)[x][y] in 'XO':
        print('Эта ячейка занята, выберите другую ')
        continue
    if turn == 'O':
        turn = 'X'
    else:
        turn = 'O'
    new_matrix = matrix_create(string)
    new_matrix[x][y] = turn
    matrix_print(new_matrix)
    string = [x for i in new_matrix for x in i]
    while string.count('X') < 3:
        break
    else:
        for i in range(8):
            if check(i)[0] == 1:
                winner = check(i)[1]
                break
