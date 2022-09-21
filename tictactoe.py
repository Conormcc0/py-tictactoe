import random

from IPython.core.display_functions import clear_output


def display_game(game_values):
    clear_output()
    print('-------------')
    print('| ' + game_values[0] + ' | ' + game_values[1] + ' | ' + game_values[2] + ' |')
    print('-------------')
    print('| ' + game_values[3] + ' | ' + game_values[4] + ' | ' + game_values[5] + ' |')
    print('-------------')
    print('| ' + game_values[6] + ' | ' + game_values[7] + ' | ' + game_values[8] + ' |')
    print('-------------')


def choose_marker():
    global player1_marker, player2_marker
    while player1_marker not in ['X', 'O']:
        player1_marker = input('Player 1: Do you want to choose X or O? ').upper()

        if player1_marker == 'X':
            player2_marker = 'O'

        if player1_marker == 'O':
            player2_marker = 'X'


def position_choice(board):
    position = 0

    while position not in range(1, 10) or not check_position_free(board, position):
        position = input("Please choose a position (1-9): ")
        if position.isdigit():
            position = int(position)

    return position - 1


def check_position_free(board, position):
    if board[position - 1] == ' ':
        return True
    return False


def replace_value(game_values, marker, position):
    game_values[position] = marker

    return game_values


def play_again():
    choice = 'invalid'

    while choice not in ['Y', 'N']:
        choice = input("Play again? (Y, N): ").upper()

    return choice == 'Y'


def full_board(board):
    for i in range(len(board) - 1):
        if check_position_free(board, i):
            return False
    return True


def check_win(board, marker):
    return (
            (board[0] == board[1] == board[2] == marker)
            or board[3] == board[4] == board[5] == marker
            or board[6] == board[7] == board[8] == marker
            or board[0] == board[3] == board[6] == marker
            or board[1] == board[4] == board[7] == marker
            or board[2] == board[5] == board[8] == marker
            or board[0] == board[4] == board[8] == marker
            or board[6] == board[4] == board[2] == marker)


while True:
    game_on = True
    win = False
    game_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player1_marker = ''
    player2_marker = ''
    turn = ""

    if random.randint(1, 2) == 1:
        turn = 'Player 1'
    else:
        turn = 'Player 2'

    choose_marker()

    while game_on:
        display_game(game_list)

        print('{}\'s turn'.format(turn))
        pos = position_choice(game_list)

        if turn == 'Player 1':
            game_list = replace_value(game_list, player1_marker, pos)
            turn = 'Player 2'
            if check_win(game_list, player1_marker):
                print('Player 1 has won!')
                display_game(game_list)
                game_on = False
            elif full_board(game_list):
                print('The game is a tie')
                break
        else:
            game_list = replace_value(game_list, player2_marker, pos)
            turn = 'Player 1'
            if check_win(game_list, player2_marker):
                print('Player 2 has won!')
                display_game(game_list)
                game_on = False
            elif full_board(game_list):
                print('The game is a tie')
                break

    if not play_again():
        break
