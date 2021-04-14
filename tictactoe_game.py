# 12-04-2021
# V1.0
# Simple Code for Tic Tac Toe
# Fabrice Lezzi
# Programming Week: 1
#
# --------- Imported Library's ---------- #
import random
# --------- Global Variables ----------- #
# Stores the game board data
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
# Stores the active player token
current_active_player = 'O'
# Indicates if game is still running, if False the program is closing
game_is_still_running = True


# ------------Defining Methods------------- #
# Prints out the board to the console
def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# Switches between the players. And falls back to make_turn
def switch_player(active_player):
    global current_active_player
    if active_player == 'X':
        current_active_player = 'O'
    else:
        current_active_player = 'X'
    print("It's " + current_active_player + "'s turn!")
    return current_active_player


# Lets the player or the computer place a token on the board.
def make_turn():

    def make_turn_ai():
        play_move_ai = random.randrange(0, 8, 1)
        if check_valid_turn(play_move_ai) is True:
            board[play_move_ai] = current_active_player
            print_board()
        else:
            make_turn_ai()

    def make_turn_human():
        print_board()
        play_move = int(input("Place your token on the board. [1-9]\n"))
        play_move = play_move - 1
        if check_valid_turn(play_move) is True:
            board[play_move] = current_active_player
            print_board()
        else:
            print("Invalid Turn.")
            make_turn_human()

    if current_active_player == 'X':
        make_turn_human()
    else:
        make_turn_ai()


# Check whether the move is legal and the selected field is free. If not: Fallback to make_turn
def check_valid_turn(move_verification):
    if board[move_verification] == '-':
        return True
    else:
        return False


# Check whether there are 3 pieces in a row, column or diagonal. If False: Fallback to switch_player
def check_for_win():
    global game_is_still_running

    def check_rows():
        global game_is_still_running
        row_1 = board[0] == board[1] == board[2] != "-"
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"

        if row_1 or row_2 or row_3:
            game_is_still_running = False
            print(current_active_player + ' has won!')
        else:
            return None

    def check_columns():
        global game_is_still_running
        column_1 = board[0] == board[3] == board[6] != "-"
        column_2 = board[1] == board[4] == board[7] != "-"
        column_3 = board[2] == board[5] == board[8] != "-"

        if column_1 or column_2 or column_3:
            game_is_still_running = False
            print(current_active_player + ' has won!')
        else:
            return None

    def check_diagonals():
        global game_is_still_running
        diagonal_1 = board[0] == board[4] == board[8] != "-"
        diagonal_2 = board[2] == board[4] == board[6] != "-"

        if diagonal_1 or diagonal_2:
            game_is_still_running = False
            print(current_active_player + ' has won!')
        else:
            return None

    def check_tie():
        global game_is_still_running
        if '-' not in board:
            game_is_still_running = False
            print("It's a tie!")
        else:
            return None

    check_rows()
    check_columns()
    check_diagonals()
    check_tie()


# Main method that accesses all other methods
def main_game():
    while game_is_still_running is True:
        switch_player(current_active_player)
        make_turn()
        check_for_win()


# ------------ Main ------------ #
if __name__ == "__main__":
    main_game()
