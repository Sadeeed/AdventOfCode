# --- Day 1: Trebuchet?! ---
# Part 2: Your calculation isn't quite right. It looks like some of the digits are
# actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid
# "digits".

from utils import get_input, parse_digits, parse_digits_regex

input_lines = get_input("input.txt")

calibration_values = []
d_list = []
for line in input_lines:
    print("Line: ", line.strip("\n"))
    digits = parse_digits(line)
    # convert digits to str
    digits = [str(digit) for digit in digits]
    print(f"Digits: {digits}")
    calibration_values.append(int(f"{digits[0]}{digits[-1]}"))
    d_list.append(digits)
print(f"Digits list: {d_list}")
print(f"Calibration values: {calibration_values}")

calibration_values_sum = sum(calibration_values)
print(f"Calibration values sum: {calibration_values_sum}")
