import re
from Utitilies import *


def part1(input_list):
    coords_count = {}
    sum = 0
    for line in input_list:
        left_coord = line.split(" -> ")[0]
        right_coord = line.split(" -> ")[1]
        x1 = int(left_coord.split(",")[0])
        y1 = int(left_coord.split(",")[1])
        x2 = int(right_coord.split(",")[0])
        y2 = int(right_coord.split(",")[1])
        if x1 != x2 and y1 != y2:
            continue
        elif y1 == y2:
            x_large = x1 if x1 > x2 else x2
            x_small = x2 if x1 > x2 else x1
            for x in range(x_small, x_large + 1):
                sum = add_to_count(coords_count, sum, x, y1)
        else:
            y_large = y1 if y1 > y2 else y2
            y_small = y2 if y1 > y2 else y1
            for y in range(y_small, y_large + 1):
                sum = add_to_count(coords_count, sum, x1, y)
    return sum


def part2(input_list):
    coords_count = {}
    sum = 0
    for line in input_list:
        left_coord = line.split(" -> ")[0]
        right_coord = line.split(" -> ")[1]
        x1 = int(left_coord.split(",")[0])
        y1 = int(left_coord.split(",")[1])
        x2 = int(right_coord.split(",")[0])
        y2 = int(right_coord.split(",")[1])
        if x1 != x2 and y1 != y2:
            x_step = 1 if x1 < x2 else -1
            y_step = 1 if y1 < y2 else -1
            length = abs(x1 - x2) + 1
            for i in range(length):
                x = x1 + i*x_step
                y = y1 + i*y_step
                sum = add_to_count(coords_count, sum, x, y)
        elif y1 == y2:
            x_large = x1 if x1 > x2 else x2
            x_small = x2 if x1 > x2 else x1
            for x in range(x_small, x_large + 1):
                sum = add_to_count(coords_count, sum, x, y1)
        else:
            y_large = y1 if y1 > y2 else y2
            y_small = y2 if y1 > y2 else y1
            for y in range(y_small, y_large + 1):
                sum = add_to_count(coords_count, sum, x1, y)
    return sum


def add_to_count(coords_count, sum, x, y):
    if (x, y) not in coords_count:
        coords_count[x, y] = 1
    else:
        coords_count[x, y] += 1
    if coords_count[x, y] == 2:
        return sum + 1
    return sum

if __name__ == "__main__":
    #input_list = parse("Day5Sample.txt")
    input_list = parse("Day5.txt")
    # print(part1(input_list))
    print(part2(input_list))