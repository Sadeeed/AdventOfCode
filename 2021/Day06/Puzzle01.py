from pathlib import Path
import numpy as np


test_input_file = Path('./2021/Day06/input_test.txt')
input_file = Path('./2021/Day06/input.txt')
lanternfish_ages = []

with open(test_input_file) as fp:
    lanternfish_ages = fp.read().split(',')

lanternfish_ages = np.array(list(map(int, lanternfish_ages)))

def total_fish(age_list, days):
    for day in range(days):
        for i in range(len(age_list)):
            if age_list[i] <= 0:
                age_list[i] = 6
                age_list = np.append(age_list, [8])
            elif age_list[i] > 0:
                age_list[i] -= 1
                
            print(age_list)

    print(len(age_list))

total_fish(lanternfish_ages, 256)