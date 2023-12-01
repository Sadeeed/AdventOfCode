from pathlib import Path
from collections import Counter

test_input_file = Path('./2021/Day03/input_test.txt')
input_file = Path('./2021/Day03/input.txt')
binary_input_list = []

with open(test_input_file) as fp:
    for line in fp:
        binary_input_list.append(line.strip('\n'))


def list_to_int(num_list):
    number = "" 
    for x in num_list: 
        number += str(x)  
    
    return int(number, 2)


def get_life_support_rating(bin_input):
    oxygen_generator_rating = []
    CO2_scrubber_rating = []
    count = Counter()
    ones = 0
    zeros = 0
    row = 0

    count_input = [list(i) for i in zip(*bin_input)]
    for num, row in count_input, range(len(count_input)):
        count = Counter(num)
        ones = count['1']
        zeros = count['0']

        oxygen_generator_rating = bin_input
        CO2_scrubber_rating = bin_input
        for i in range(len(bin_input)):
            if ones > zeros:
                if oxygen_generator_rating[row] == 0:
                    del oxygen_generator_rating[j]
            elif zeros > ones:
                if oxygen_generator_rating[j][row] == 1:
                    del oxygen_generator_rating[j]
            elif zeros == ones:
                if oxygen_generator_rating[j][row] == 0:
                    del oxygen_generator_rating[j]


    # Oxygen Generator Rating
    # for i in range(len(oxygen_generator_rating[0])):
    #     for j in range(len(oxygen_generator_rating)):
    #         if oxygen_generator_rating[j][i] == 1:
    #             ones += 1
    #         elif oxygen_generator_rating[j][i] == 0:
    #             zeros += 1

        
        
    #     for j in range(len(oxygen_generator_rating)):
    #         if ones > zeros:
    #             if oxygen_generator_rating[j][row] == 0:
    #                 del oxygen_generator_rating[j]
    #         elif zeros > ones:
    #             if oxygen_generator_rating[j][row] == 1:
    #                 del oxygen_generator_rating[j]
    #         elif zeros == ones:
    #             if oxygen_generator_rating[j][row] == 0:
    #                 del oxygen_generator_rating[j]

    #     ones = 0
    #     zeros = 0
    #     row += 1

    # ogr = list_to_int(oxygen_generator_rating)
    # # epsilon = list_to_int(epsilon_value)
    # print(f"Oxygen Generator Rating: {ogr}")
    # # print(f"Epsilon: {epsilon}")
    # # print(f"Power Consumption: {gamma * epsilon}")
         


# with open(input_file) as fh:
#     m = [a.strip() for a in fh.readlines()]

# # Part 2
# # for oxygen: switch = True
# # for co2: switch = False
# def rating(gas, switch):
#     i = 0
#     while len(gas) > 1:
#         freq = Counter([x[i] for x in gas]).most_common()
#         if (freq[0][1] == freq[1][1]) == switch:
#             # oxygen: case when frequencies match: use '1'; last one since sorted alphanumerically
#             # co2: pick the least common, always the last one
#             bit = freq[-1][0]
#         else:
#             # oxygen: pick the most common, always the first one
#             # co2: case when frequencies match: use '0'; first one since sorted alphanumerically
#             bit = freq[0][0]
#         gas = list(filter(lambda x: x[i] == bit, gas))
#         i += 1
#     return int(gas[0], 2)

# oxygen = rating(m, True)
# co2 = rating(m, False)
# print(f"Life support rating: {oxygen * co2}")


# get_life_support_rating(binary_input_list)


