import re
from Utitilies import *


def part1(input_list):
    board_to_rowcol = []
    used_numbers = set()

    number_sequence = [int(x) for x in input_list[0].split(',')]
    for index, board in enumerate(input_list[1:]):
        if index == len(board_to_rowcol):
            board_to_rowcol.append([])
        formatted_board = [[int(y) for y in re.sub(' +', ' ', x).strip().split(" ")] for x in board.split("\n")]
        board_to_rowcol[index].extend(formatted_board)
        for i in range(5):
            board_to_rowcol[index].append([formatted_board[0][i], formatted_board[1][i], formatted_board[2][i], formatted_board[3][i], formatted_board[4][i]])

    for i in range(4):
        used_numbers.add(number_sequence.pop(0))

    while True:
        winning_number = number_sequence.pop(0)
        used_numbers.add(winning_number)

        for board in board_to_rowcol:
            for rowcol in board:
                count = 0
                for number in rowcol:
                    if number not in used_numbers:
                        break
                    count += 1
                if count == 5:
                    sum = 0
                    for i in range(5):
                        for j in range(5):
                            if board[i][j] not in used_numbers:
                                sum += board[i][j]
                    return sum * winning_number


def part2(input_list):
    board_to_rowcol = []
    used_numbers = set()

    number_sequence = [int(x) for x in input_list[0].split(',')]
    for index, board in enumerate(input_list[1:]):
        if index == len(board_to_rowcol):
            board_to_rowcol.append([])
        formatted_board = [[int(y) for y in re.sub(' +', ' ', x).strip().split(" ")] for x in board.split("\n")]
        board_to_rowcol[index].extend(formatted_board)
        for i in range(5):
            board_to_rowcol[index].append(
                [formatted_board[0][i], formatted_board[1][i], formatted_board[2][i], formatted_board[3][i],
                 formatted_board[4][i]])

    for i in range(4):
        used_numbers.add(number_sequence.pop(0))

    while True:
        winning_number = number_sequence.pop(0)
        used_numbers.add(winning_number)
        boards_to_be_deleted = []

        for index, board in enumerate(board_to_rowcol):
            outer_break = False
            for rowcol in board:
                count = 0
                for number in rowcol:
                    if number not in used_numbers:
                        break
                    count += 1
                if count == 5:
                    if len(board_to_rowcol) == 1:
                        sum = 0
                        for i in range(5):
                            for j in range(5):
                                if board[i][j] not in used_numbers:
                                    sum += board[i][j]
                        return sum * winning_number
                    else:
                        boards_to_be_deleted.append(index)
                        outer_break = True
                if outer_break:
                    break

        for index, board_number in enumerate(boards_to_be_deleted):
            board_to_rowcol.pop(board_number - index)



if __name__ == "__main__":
    # input_list = parse("Day4Sample.txt", "\n\n")
    input_list = parse("Day4.txt", "\n\n")
    # print(part1(input_list))
    print(part2(input_list))