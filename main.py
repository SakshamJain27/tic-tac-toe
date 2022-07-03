def check():
    wins = [[0, 1, 2],[3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (x_state[win[0]]+x_state[win[1]]+x_state[win[2]]) == 3:
            print("X wins")
            quit()
        elif (y_state[win[0]] + y_state[win[1]] + y_state[win[2]]) == 3:
            print("o wins")
            quit()


def print_board():
    one = 'X' if x_state[0] else('O' if y_state[0] else ' ')
    two = 'X' if x_state[1] else('O' if y_state[1] else ' ')
    three = 'X' if x_state[2] else('O' if y_state[2] else ' ')
    four = 'X' if x_state[3] else('O' if y_state[3] else ' ')
    five = 'X' if x_state[4] else('O' if y_state[4] else ' ')
    six = 'X' if x_state[5] else('O' if y_state[5] else ' ')
    seven = 'X' if x_state[6] else('O' if y_state[6] else ' ')
    eight = 'X' if x_state[7] else('O' if y_state[7] else ' ')
    nine = 'X' if x_state[8] else('O' if y_state[8] else ' ')
    print()
    print(f" {one} | {two} | {three} ")
    print("---+---+---")
    print(f" {four} | {five} | {six} ")
    print("---+---+---")
    print(f" {seven} | {eight} | {nine} ")
    print()


def on_start():
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 ")
    print()


if __name__ == "__main__":
    x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # X for 1 and 0 for O
    print("Welcome to tic-tac-toe")
    print("This are the positions\n")
    while True:
        on_start()
        print_board()
        if turn == 1:
            print("X's chance")
            choice = int(input("Enter the position"))
            x_state[choice] = 1
            turn = 0
            print_board()
            on_start()
            check()
        if turn == 0:
            print("O's chance")
            choice = int(input("Enter the position"))
            y_state[choice] = 1
            turn = 1
            check()
