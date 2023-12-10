from utils import get_input, parse_input, get_total_steps

lines = get_input('input.txt')

data = parse_input(lines)
steps = get_total_steps(data)

print(f'Took {steps} steps to reach ZZZ')
