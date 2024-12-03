from utils import get_input
import re

input = get_input('input.txt')

def parse_input(input):
    return re.findall(r"(?:mul\(\d+,\d+\))", input)

def multiply(operation):
    print(f"Operation: {operation}")
    a, b = map(int, re.findall(r"\d+", operation))
    print(f"a: {a}, b: {b}")
    result = a * b
    print(f"Result: {result}")
    return result
sum = 0
for line in input:
    print(f"Line: {line}")
    parsed_line = parse_input(line)
    print(f"Parsed: {parsed_line}")
    for operation in parsed_line:
        result = multiply(operation)
        sum += result
print(f"Sum: {sum}")
