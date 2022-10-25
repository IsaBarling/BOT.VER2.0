
import sys
from random import randint


VERTICAL_COORDINATS = ('a', 'b', 'c')
EMPTY_CHAR = '_'
AI_TURN = True
USER_TURN = False


def show_field(field):
    arr = ['|  ', '1', '2', '3']
    output = '\t' + ' '.join(arr)
    #print(' ', '1', '2', '3')
    for y, v in enumerate(VERTICAL_COORDINATS):
        #print(v, ' '.join(field[y]))
        output += '\n|' + v + " " + ' '.join(field[y])
    return output

def is_draw(field):
    count = 0
    for y in range(3):
        count += 1 if EMPTY_CHAR in field[y] else 0
    return count == 0


def set_user_position(coordinats):
    real_x, real_y = 0, 0
    y, x = tuple(coordinats)
    if int(x) not in (1, 2, 3) or y not in VERTICAL_COORDINATS:
        return([1,'Not valid coordinats'])
    real_x, real_y = int(x) - 1, VERTICAL_COORDINATS.index(y)
    if field[real_y][real_x] == EMPTY_CHAR:
        field[real_y][real_x] = user_char
        return([0, ''])
    else:
        return([2], 'Wrong move! Try again!')
    

def get_opponent_char(char):
    return '0' if char == 'x' else 'x'


def is_win(char, field):
    opponent_char = get_opponent_char(char)
    # проверяем строки
    for y in range(3):
        if opponent_char not in field[y] and EMPTY_CHAR not in field[y]:
            return True

    # проверяем колонки
    for x in range(3):
        col = [field[0][x], field[1][x], field[2][x]]
        if opponent_char not in col and EMPTY_CHAR not in col:
            return True

    # проверяем диагонали
    diagonal = [field[0][0], field[1][1], field[2][2]]
    if opponent_char not in diagonal and EMPTY_CHAR not in diagonal:
        return True
    diagonal = [field[0][2], field[1][1], field[2][0]]
    if opponent_char not in diagonal and EMPTY_CHAR not in diagonal:
        return True

    return False


def minimax(board, depth, is_ai_turn):
    if is_win(computer_char, board):
        return scores[computer_char]
    if is_win(user_char, board):
        return scores[user_char]
    if is_draw(board):
        return scores['draw']

    if is_ai_turn:
        # выбираем ход который нам выгодней
        best_score = - sys.maxsize
        for y in range(3):
            for x in range(3):
                if board[y][x] == EMPTY_CHAR:
                    board[y][x] = computer_char
                    score = minimax(board, depth + 1, USER_TURN)
                    board[y][x] = EMPTY_CHAR
                    best_score = max(best_score, score)
    else:
        # противник выбирает ход который нам не выгоден
        best_score = sys.maxsize
        for y in range(3):
            for x in range(3):
                if board[y][x] == EMPTY_CHAR:
                    board[y][x] = user_char
                    score = minimax(board, depth + 1, AI_TURN)
                    board[y][x] = EMPTY_CHAR
                    best_score = min(best_score, score)
    return best_score


def get_computer_position(field):
    move = None
    best_score = -sys.maxsize
    board = [field[y].copy() for y in range(3)]
    for y in range(3):
        for x in range(3):
            if board[y][x] == EMPTY_CHAR:
                board[y][x] = computer_char
                score = minimax(board, 0, USER_TURN)
                board[y][x] = EMPTY_CHAR
                if score > best_score:
                    best_score = score
                    move = (x, y)

    return move




user_char = "x"
computer_char = get_opponent_char(user_char)

scores = {
    user_char: -100,
    computer_char: 100,
    'draw': 0
}

