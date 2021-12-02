from pathlib import Path

test_input_file = Path('./2021/Day02/input_test.txt')
input_file = Path('./2021/Day02/input.txt')
command_list = []

with open(input_file) as fp:
    for line in fp:
        command_list.append(line.strip('\n'))


def calculate_final_product(commands):
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        command = command.split(' ')
        if command[0] == 'forward':
            horizontal_position += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == 'up':
            aim -= int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])

    print(f"Horizontal Position: {horizontal_position}")
    print(f"Depth: {depth}")

    return f"Final Product: {horizontal_position*depth}"

print(calculate_final_product(command_list))