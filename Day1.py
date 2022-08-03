from Utitilies import *


def part1(input_list):
    count = 0
    for index, depth in enumerate(input_list):
        if index != 0 and int(input_list[index]) > int(input_list[index - 1]):
            count += 1
    return count


def part2(input_list):
    count = -1
    previous_sum = 0
    for index, depth in enumerate(input_list):
        if index >= 2:
            current_sum = int(input_list[index]) + int(input_list[index - 1]) + int(input_list[index - 2])
            if current_sum > previous_sum:
                count += 1
            previous_sum = current_sum
    return count


if __name__ == "__main__":
    input_list = parse("Day1.txt")
    print(part2(input_list))