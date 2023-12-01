import re


def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
    return lines


def parse_digits(line):
    """
    Parse 1-digit numbers from the provided line, numbers in the input can also be spelled out.
    :param line:
    :return: List of integers
    """
    # matches = re.findall(r'\d|\w{3,5}', line)
    digits_spelled_out = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    digits = []
    for line_index in range(len(line)):
        letter = line[line_index]
        if letter.isdigit():
            digits.append(int(letter))
        elif letter.isalpha():
            if letter.lower() in [key[0] for key in digits_spelled_out.keys()]:
                # get keys starting with letter
                keys = [key for key in digits_spelled_out.keys() if key[0] == letter.lower()]
                for key in keys:
                    if line[line_index:line_index + len(key)] == key:
                        digits.append(digits_spelled_out[key])
                        line_index += len(key) - 2
                        break
    return digits


def parse_digits_regex(line):
    """
    Parse 1-digit numbers from the provided line, numbers in the input can also be spelled out.
    :param line:
    :return: List of integers
    """
    digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    digits_spelled_out = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    for digit in digits:
        if digit.isalpha():
            digits[digits.index(digit)] = digits_spelled_out[digit]

    return digits
