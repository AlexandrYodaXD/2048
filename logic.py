import random


def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)


def get_number_from_index(i, j):
    return i * 4 + j + 1


def get_index_from_number(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def insert_2_or_4(mas, x, y):
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def is_zero_in_mas(mas):
    for row in mas:
        if 0 in row:
            return True
    return False


def add_num(mas):
    empty_list = get_empty_list(mas)
    random_block_num = random.choice(empty_list)
    x, y = get_index_from_number(random_block_num)
    mas = insert_2_or_4(mas, x, y)
    print(f'Мы заполнили элемент под номером {random_block_num}')
    return mas

def move_left(mas):
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(len(mas)):
        for j in range(len(mas) - 1):
            if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                mas[i].pop(j + 1)
                mas[i].append(0)
    return mas


def move_right(mas):
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(len(mas)):
        for j in range(len(mas) - 1, 0, -1):
            if mas[i][j] == mas[i][j - 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                mas[i].pop(j - 1)
                mas[i].insert(0, 0)
    return mas

def turn_left(mas):
    res_mas = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            res_mas[i][j] = mas[j][-i-1]
    return res_mas

def turn_right(mas):
    res_mas = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            res_mas[i][j] = mas[-j-1][i]
    return res_mas

def move_up(mas):
    turned_mas = turn_right(mas)
    new_mas = move_right(turned_mas)
    turned_back = turn_left(new_mas)
    return turned_back

def move_down(mas):
    turned_mas = turn_left(mas)
    new_mas = move_right(turned_mas)
    turned_back = turn_right(new_mas)
    return turned_back
