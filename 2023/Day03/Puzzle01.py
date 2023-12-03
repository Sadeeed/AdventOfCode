# --- Day 3: Gear Ratios ---
# Part 1

from utils import get_input, get_part_numbers
import re

lines = get_input('input.txt')
part_numbers = get_part_numbers(lines)


print("Part numbers: ", part_numbers)
sum_of_part_numbers = sum(part_numbers)
print("Sum of part numbers: ", sum_of_part_numbers)
