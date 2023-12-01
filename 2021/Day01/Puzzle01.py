from pathlib import Path

input_file = Path('./2021/Day01/input.txt')
input_list = []

with open(input_file) as fp:
    for line in fp:
        input_list.append(int(line.strip('\n')))

def check_increased_measurement(measurements):
    maximum = input_list[0]
    count = []
    for x in input_list:
        if x > maximum:
            maximum = x
            count.append(maximum)
        else:
            maximum = x
    return len(count)

print(check_increased_measurement(input_list))