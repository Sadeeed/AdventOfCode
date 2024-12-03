from utils import get_input
import re

input = get_input('input.txt')

def parse_input(input, is_enabled=True):
    if is_enabled:
        input = "do()" + input
    input = input.replace("don't()", "MDISABLED").replace("do()", "MENABLED")
    input_tokens = input.split("M")
    enabled_operations = []
    for token in input_tokens:
        if token.startswith("ENABLED"):
            is_enabled = True
            enabled_operations.extend(re.findall(r"(?:mul\(\d+,\d+\))", token))
        else:
            is_enabled = False
    print(f"Input Tokens: {input_tokens}")
    print(f"Is Enabled: {is_enabled}")
    print(f"Enabled Operations: {enabled_operations}")
    return enabled_operations, is_enabled

def multiply(operation):
    a, b = map(int, re.findall(r"\d+", operation))
    result = a * b
    print(f"Operation: {operation} Result: {result}")
    return result


sum = 0
is_enabled = True
for line in input:
    print(f"Line: {line}")
    parsed_line, is_enabled = parse_input(line, is_enabled)
    for operation in parsed_line:
        result = multiply(operation)
        sum += result
print(f"Sum: {sum}")
