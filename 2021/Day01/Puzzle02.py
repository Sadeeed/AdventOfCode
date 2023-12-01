from pathlib import Path

test_input_file = Path('./2021/Day01/input_test.txt')
input_file = Path('./2021/Day01/input.txt')
input_list = []

with open(input_file) as fp:
    for line in fp:
        input_list.append(int(line.strip('\n')))

def find_sum_of_measurement_increments(measurements):
    sum_list = []
    for i in range(len(measurements)-2):
        sum_list.append(measurements[i] + measurements[i+1] + measurements[i+2])
    
    return sum_list

def count_increments(sum_list):
    count = 0
    for i in range(len(sum_list)):
        if sum_list[i] > sum_list[i-1]:
            count += 1
    
    return count
        

increment_list = find_sum_of_measurement_increments(input_list)
print(count_increments(increment_list))