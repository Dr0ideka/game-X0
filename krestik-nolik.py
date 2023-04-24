board = [1,2,3,4,5,6,7,8,9]
board_size = 3

def game_board():
    "Игровое поле"
    print("_" * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|' )*3)
        print('',board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print(('_'*3+'|')*3)
    pass
def check_move(index_x0,char):
    "Делаем ход"
    if (index_x0 > 9 or index_x0 < 1 or board[index_x0-1] in ('X', 'O')):
        return False

    board[index_x0 - 1] = char
    return True

def check_winner():
    win = False

    win_comb = (
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0, 4, 8),(2,4,6)
    )
    for pos in win_comb:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win

def start_game():
    player_x = 'X'
    step = 1
    game_board()

    while (step<10) and (check_winner() == False):
        index_x0 = int(input('ход:' + player_x + ',введите номер поля или чтобы закончить "0":'))

        if (index_x0 == "0"):
            break


        if (check_move(int(index_x0), player_x)):
            print('готово')
            if (player_x == 'X'):
                player_x = 'O'
            else:
                player_x = 'X'


            game_board()
            step += 1
        else:
            print('попробуйте другую цифру')

    if (step == 10):
        print('ничья')
    else:
        print('Победил:'+ check_winner())

print('Игра началась')
start_game()
