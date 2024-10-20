from itertools import filterfalse

board_size = 3 #количество клеток
board = [1,2,3,4,5,6,7,8,9] #игровое поле
def draw_board():
    """Выводим игровое поле"""
    print('_' * 4 * board_size) #вывод верхнего горизонтального разделителя
    for i in range(board_size):
        print((' '*3 + '|')*3) #вывод вертикальных разделителей
        print('',board[i*3], '|', board[1+ i*3], '|', board[2+ i*3], '|') #вывод цифр
        print(('_' * 3 + '|') * 3) #вывод горизонтальных разделителей
    pass
def game_step(index, char): #индекс куда совершается код, символ текущего игрока
    """Выполняем ход"""
    if (index>9) or (index <1) or (board[index-1] in ('X', 'O')): #проверяем чтобы введенное число было в диапазоне и чтобы ячейка не была заняла
        return False
    board[index-1]=char #заменяет символ в ячейке на наш
    return True
    pass
def check_win():
    """Проверка на победу"""
    win=False

    win_combination= (
        (0,1,2), (3,4,5), (6,7,8), #горизонтальные
        (0,3,6), (1,4,7), (2,5,8), #вертикальные
        (0,4,8), (2,4,6) #диагональные
    )
    for i in win_combination:
        if (board[i[0]]==board[i[1]]) and (board[i[1]]==board[i[2]]):
            win = board[i[0]]
    return win
    pass
def start_game():
    """Последовательный вывод функций"""
    current_player = 'X' #хранит ход текущего игрока
    step = 1 #номер шага
    draw_board()

    while (step < 10) and (check_win() == False):
        index = input('Ходит игрок '+ current_player + '. Введите номер поля (0 - выход): ')
        if index=='0':
            break
        if game_step(int(index), current_player):
            print('Ход записался')

            if current_player=='X': #замена крестика на нолик
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            step += 1 #увеличен номер хода
        else:
            print('Неверный номер, повторите')

    if step==10:
        print('Игра окончена, ничья!')
    else:
        print('Выиграл ' + check_win() )
print('Приветствуем вас в крестиках ноликах!')
start_game()



