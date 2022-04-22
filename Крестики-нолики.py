# КРЕСТИКИ - НОЛИКИ

def greet():
    print("Привет. Введите поле, куда Вы хотите поставить "
          "\nкрестик или нолик по формату: 1 1 или 2 3 или 3 1."
          "\nСначала идет номер строки, затем номер столбца. Вводить через пробел")


board = [[" ", "1", "2", "3"],
         [1, "-", "-", "-"],
         [2, "-", "-", "-"],
         [3, "-", "-", "-"]]


def print_board(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()


def check_board_and_input():
    while True:
        square = input("Введите поле, куда поставить х или о: ").split()

        if len(square) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = square

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 3 or 0 > y or y > 3:
            print(" Координаты вне диапазона! ")
            continue

        if board[x][y] != "-":
            print(" Клетка занята! ")
            continue
        return x, y


def check_win():
    win = [[board[1][1], board[1][2], board[1][3]], [board[2][1], board[2][2], board[2][3]],
           [board[3][1], board[3][2], board[3][3]], [board[1][1], board[2][1], board[3][1]],
           [board[1][2], board[2][2], board[3][2]], [board[1][3], board[2][3], board[3][3]],
           [board[1][1], board[2][2], board[3][3]], [board[3][1], board[2][2], board[1][3]]]
    for i in win:
        if i == ["X", "X", "X"]:
            print("Победил Х")
            return True
        if i == ["0", "0", "0"]:
            print("Победил 0")
            return True
    return False


# Игра:
num_of_moves = 0
greet()

while True:
    num_of_moves += 1
    print_board(board)

    if num_of_moves % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = check_board_and_input()

    if num_of_moves % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if check_win():
        print_board(board)
        break

    if num_of_moves == 9:
        print("Ничья!")
        break
