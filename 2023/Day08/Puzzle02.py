from utils import get_input, parse_input, get_total_steps_p2
from itertools import cycle
from math import lcm

lines = get_input('input.txt')

data = parse_input(lines)

start_nodes = [key for key in data['nodes'].keys() if key[-1] == 'A']

instruction_map = {
    'R': 1,
    'L': 0,
}

steps = [get_total_steps_p2(start_node, data) for start_node in start_nodes]
steps = lcm(*steps)

print(f'Took {steps} steps to reach Z on all nodes')
