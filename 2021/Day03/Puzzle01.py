from pathlib import Path

test_input_file = Path('./2021/Day03/input_test.txt')
input_file = Path('./2021/Day03/input.txt')
binary_input_list = []

with open(input_file) as fp:
    for line in fp:
        binary_input_list.append(line.strip('\n'))


def get_power_consumption(bin_input):
    new_list = []
    gamma_value = []
    epsilon_value = []
    ones = 0
    zeros = 0

    for num in bin_input:
        new_list.append([int(i) for i in num])

    for i in range(len(new_list[0])):
        for j in range(len(new_list)):
            if new_list[j][i] == 1:
                ones += 1
            elif new_list[j][i] == 0:
                zeros += 1
        if ones > zeros:
            gamma_value.append(1)
            epsilon_value.append(0)
        else:
            gamma_value.append(0)
            epsilon_value.append(1)
        ones = 0
        zeros = 0

    gamma = list_to_int(gamma_value)
    epsilon = list_to_int(epsilon_value)
    print(f"Gamma: {gamma}")
    print(f"Epsilon: {epsilon}")
    print(f"Power Consumption: {gamma * epsilon}")


def list_to_int(num_list):
    number = "" 
    for x in num_list: 
        number += str(x)  
    
    return int(number, 2)

            

get_power_consumption(binary_input_list)
