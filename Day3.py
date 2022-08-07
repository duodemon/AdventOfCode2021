from Utitilies import *


def part1(input_list):
    bit_count_list = []
    for bit in input_list[0]:
        bit_count_list.append(0)
    for number in input_list:
        for pos, bit in enumerate(number):
           if bit == "0":
               bit_count_list[pos] -= 1
           elif bit == "1":
               bit_count_list[pos] += 1
    gamma_rate = ""
    epsilon_rate = ""
    for count in bit_count_list:
        if count < 0:
            gamma_rate += "0"
            epsilon_rate += "1"
        elif count > 0:
            gamma_rate += "1"
            epsilon_rate += "0"
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(input_list):
    current_pos = 0
    oxygen_gen_rating_list = input_list[:]
    while len(oxygen_gen_rating_list) != 1:
        count = get_bit_count(oxygen_gen_rating_list, current_pos)
        if count < 0:
            bit = "0"
        else:
            bit = "1"
        oxygen_gen_rating_list = [x for x in oxygen_gen_rating_list if x[current_pos] == bit]
        current_pos += 1

    CO2_scrubber_rating_list = input_list[:]
    current_pos = 0
    while len(CO2_scrubber_rating_list) != 1:
        count = get_bit_count(CO2_scrubber_rating_list, current_pos)
        if count < 0:
            bit = "1"
        else:
            bit = "0"
        CO2_scrubber_rating_list = [x for x in CO2_scrubber_rating_list if x[current_pos] == bit]
        current_pos += 1

    return int(oxygen_gen_rating_list[0], 2) * int(CO2_scrubber_rating_list[0], 2)


def get_bit_count(bit_list, current_pos):
    count = 0
    for number in bit_list:
        if number[current_pos] == "0":
            count -= 1
        elif number[current_pos] == "1":
            count += 1
    return count

if __name__ == "__main__":
    # input_list = parse("Day3Sample.txt")
    input_list = parse("Day3.txt")
    # print(part1(input_list))
    print(part2(input_list))