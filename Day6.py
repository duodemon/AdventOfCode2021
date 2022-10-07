import re
from Utitilies import *


def part1(input_list):
    fish_list = [int(x) for x in input_list]
    for i in range(80):
        num_fish_to_add = 0
        for index, value in enumerate(fish_list):
            if fish_list[index] == 0:
                fish_list[index] = 6
                num_fish_to_add += 1
            else:
                fish_list[index] -= 1
        for fish in range(num_fish_to_add):
            fish_list.append(8)
    return len(fish_list)


def part2(input_list):
    fish_list = [int(x) for x in input_list]
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for timer in fish_list:
        counts[timer] += 1
    for i in range(256):
        counts = counts[1:7] + [counts[0] + counts[7], counts[8], counts[0]]
    return sum(counts)


if __name__ == "__main__":
    # input_list = parse("Day6Sample.txt", ",")
    input_list = parse("Day6.txt", ",")
    # print(part1(input_list))
    print(part2(input_list))