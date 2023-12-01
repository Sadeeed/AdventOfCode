# --- Day 1: Trebuchet?! ---
# Part 1: Find the calibration values in the input file and sum them.

import re
from utils import get_input

lines = get_input("input.txt")
calibration_values = []
for line in lines:
    digits = re.findall(r'\d', line)
    calibration_values.append(int(f"{digits[0]}{digits[-1]}"))
calibration_values_sum = sum(calibration_values)
print(f"Calibration values sum: {calibration_values_sum}")
