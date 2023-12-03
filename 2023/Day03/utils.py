import re

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '?', '_', '=', ',', '<', '>', '/']


def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
        lines = [line.strip() for line in lines]
    return lines


def get_part_numbers(lines):
    part_numbers = []
    for index, line in enumerate(lines):
        part_number = ''
        for match in re.finditer(r'\d+', line):
            start_index = match.start()
            end_index = match.end() - 1
            if start_index - 1 >= 0 and lines[index][start_index - 1] in special_characters:
                part_numbers.append(int(match.group()))
            if end_index + 1 < len(lines[0]) and lines[index][end_index + 1] in special_characters:
                part_numbers.append(int(match.group()))
            for j in range(start_index - 1, end_index + 2):
                if j < 0 or j >= len(lines[0]):
                    continue
                if index - 1 > 0 and lines[index - 1][j] in special_characters:
                    part_numbers.append(int(match.group()))
                if index + 1 < len(lines[0]) and lines[index + 1][j] in special_characters:
                    part_numbers.append(int(match.group()))

    return part_numbers
