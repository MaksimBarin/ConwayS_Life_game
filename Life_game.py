# https://bitstorm.org/gameoflife/

# 1. Если у живой клетки меньше 2 соседей, она умирает от одиночества
# 2. Если у живой клетки 2 или 3 соседа, она продолжает жить
# 3. Если у клетки более 3 соседей, она умирает от перенаселения
# 4. Если у неживой клетки ровно 3 соседа, происходит размножение и клетка становится живой

'''
Игра запускается через командную строку
'''

from random import randint, choice
import os


def get_size():
    correct = False
    while not correct:
        print("Пожалуйста, введите 2 значения, чтобы задать размерность поля симуляции.")
        n = input('n: ')
        m = input('m: ')
        if n.isdigit() and m.isdigit():
            n, m = int(n), int(m)
            if 0 < n < 31 and 0 < m < 31:
                correct = True
            else:
                print("--= значения должны лежать в промежутке [1-30] =--")
    return n, m

# Функция для генерации следующего состояния
def next_gen(lst):
    neibs = 0
    lgth = len(lst)
    lst1 = [['.' for i in range(len(lst[j]))] for j in range(lgth)]
    for i in range(lgth):
        line_l = len(lst[i])
        for j in range(line_l):
            neibs = lst[i-1][j-1]     +      lst[i][j-1]     +      lst[i-(lgth-1)][j-1] + \
                    lst[i-1][j]                  +                  lst[i-(lgth-1)][j]   + \
                    lst[i-1][j-(line_l-1)] + lst[i][j-(line_l-1)] + lst[i-(lgth-1)][j-(line_l-1)]
            neibs = neibs.count('o')
            if lst[i][j] == 'o':
                if neibs == 3 or neibs == 2:
                    lst1[i][j] = 'o'
            else:
                if neibs == 3:
                    lst1[i][j] = 'o'
            neibs = 0
    return lst1

# Функция для отображения поля
def show(lst):
    for row in lst:
        print(*row, sep=' ', end='\n')


# Функция для чтения матрицы из текстового файла
def read_file():
    lst = []
    with open('Lst_Of_Life.txt', 'r') as file:
        for line in file:
            lst.append(line.split())
    return lst

# Функция для записи нового состояния в текстовый файл
def write_file(file_name = 'Lst_Of_Life.txt'):
    with open(file_name, 'w') as file:
        for row in lst:
            file.write(' '.join(row) + '\n')

# Функция для обнуления матрицы
def zero_file(file_name = 'Lst_Of_Life.txt'):
    string = ('. ' * (len(lst[0]) - 1) + '.\n') * len(lst)
    with open(file_name, 'w') as file:
        file.write(string)

# Функция для генерации случайной матрицы
def random_generation(n=30, m=30):
    return [[choice(('o', '.')) for i in range(n)] for j in range(m)]

# Функция для ввода матрицы с клавиатуры
def key_generation():
    n, m = get_size()
    print("подсказка: вводите поле построчно, разделяйте клетки пробелами\n")
    lst = [[s for s in input().split()] for k in range(m)]
    for i in range(len(lst)):
        if len(lst[i]) != n:
            print('Error')
            return []
        else:
            return lst


os.system('CLS')

hello_info = '''
Данный симулятор будет демонстрировать жизнь клеток, живущих по таким правилам:
    1. Если у живой клетки меньше 2 соседей, она умирает от одиночества
    2. Если у живой клетки 2 или 3 соседа, она продолжает жить
    3. Если у клетки более 3 соседей, она умирает от перенаселения
    4. Если у неживой клетки ровно 3 соседа, происходит размножение и клетка становится живой
[клетки -> живая 'o' и мертвая '.']
\n      Так выглядит поле максимального размера 30х30 :\n'''

options = \
'''
          +++ выберите действие +++
1) сгенерировать новое поколение  - нажмите Enter,
2) создать случайное поле (30х30) - введите 1,
3) создать поле желаемых размеров - введите 2 (ввод клеток осуществляется вручную),
4) убрать все живые клетки с поля - введите 3,
5) выйти                          - введите 0.
\n>>> '''

print(hello_info)

# Создание и отрисовка начального состояния
lst = random_generation()
write_file()
show(lst)

# Основной цикл игры
while True:
    # Информация о выборе игрока и следующем действии
    action = input(options)
    if action == '':
        lst = read_file()
        lst = next_gen(lst)
        write_file()
    elif action == '1':
        lst = random_generation()
        write_file()
    elif action == '2':
        lst = key_generation()
        if not lst:
            lst = random_generation()
        write_file()
        print()
    elif action == '3':
        zero_file()
        lst = read_file()
    elif action == '0':
        print('\nЗахочется ещё - знаешь где найти\n')
        break
    else:
        print('Можно использовать только команды из списка.')
    os.system('CLS')
    show(lst)