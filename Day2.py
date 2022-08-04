from Utitilies import *


def part1(input_list):
    depth = 0
    hor_pos = 0
    for command in input_list:
        command_list = command.split(" ")
        if command_list[0] == "up":
            depth -= int(command_list[1])
        elif command_list[0] == "down":
            depth += int(command_list[1])
        else:
            hor_pos += int(command_list[1])
    return depth * hor_pos


def part2(input_list):
    depth = 0
    hor_pos = 0
    aim = 0
    for command in input_list:
        command_list = command.split(" ")
        if command_list[0] == "up":
            aim -= int(command_list[1])
        elif command_list[0] == "down":
            aim += int(command_list[1])
        else:
            depth += int(command_list[1]) * aim
            hor_pos += int(command_list[1])
    return depth * hor_pos


if __name__ == "__main__":
    # input_list = parse("Day2Sample.txt")
    input_list = parse("Day2.txt")
    # print(part1(input_list))
    print(part2(input_list))