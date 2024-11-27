import random
import os

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_random_number(board)
    add_random_number(board)
    return board

def add_random_number(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("\t".join(str(num) if num != 0 else '.' for num in row))
    print()

def slide_and_merge(row):
    new_row = [num for num in row if num != 0]
    merged_row = []
    skip = False

    for i in range(len(new_row)):
        if skip:
            skip = False
            continue
        if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
            merged_row.append(new_row[i] * 2)
            skip = True
        else:
            merged_row.append(new_row[i])

    merged_row.extend([0] * (4 - len(merged_row)))
    return merged_row

def move_left(board):
    for i in range(4):
        board[i] = slide_and_merge(board[i])

def move_right(board):
    for i in range(4):
        board[i] = slide_and_merge(board[i][::-1])[::-1]

def move_up(board):
    board[:] = list(map(list, zip(*board)))  # Transpose
    move_left(board)
    board[:] = list(map(list, zip(*board)))  # Transpose back

def move_down(board):
    board[:] = list(map(list, zip(*board)))  # Transpose
    move_right(board)
    board[:] = list(map(list, zip(*board)))  # Transpose back

def check_game_over(board):
    if any(0 in row for row in board):
        return False
    for i in range(4):
        for j in range(4):
            if (i < 3 and board[i][j] == board[i + 1][j]) or (j < 3 and board[i][j] == board[i][j + 1]):
                return False
    return True

def main():
    board = initialize_board()
    print_board(board)

    while True:
        move = input("Use WASD to move (W=up, A=left, S=down, D=right): ").upper()
        if move == 'W':
            move_up(board)
        elif move == 'S':
            move_down(board)
        elif move == 'A':
            move_left(board)
        elif move == 'D':
            move_right(board)
        else:
            print("Invalid input! Please use W, A, S, or D.")
            continue

        add_random_number(board)
        print_board(board)

        if check_game_over(board):
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
