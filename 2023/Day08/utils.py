from itertools import cycle

instruction_map = {
    'R': 1,
    'L': 0,
}

def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
        lines = [line.strip() for line in lines]
    return lines


def parse_input(input_list):
    instructions = []
    nodes = {}
    for item in input_list:
        if '=' not in item:  # This is an instruction
            instructions.extend(list(item))
        else:  # This is a node definition
            key, value = item.split('=')
            key = key.strip()
            value = [value.strip() for value in value.strip().replace('(', '').replace(')', '').split(',')]
            nodes[key] = value
    return {'instructions': instructions, 'nodes': nodes}


def get_total_steps(data):
    cycle_instructions = cycle(data['instructions'])
    steps = 0
    start_node = "AAA"

    for index, instruction in enumerate(cycle_instructions):
        print(f"Instruction: {instruction} Map: {instruction_map[instruction]}, Start Node: {start_node}")
        if start_node == 'ZZZ':
            steps = index
            break
        start_node = data['nodes'][start_node][instruction_map[instruction]]
    
    return steps


def get_total_steps_p2(start_node, data):
    # for index, instruction in enumerate(cycle_instructions):
    #     # print(f"Instruction: {instruction} Map: {instruction_map[instruction]}, Start Node: {start_node}")
    #     if start_node[-1] == 'Z':
    #         # print(f"In {index} steps, we reached Z")
    #         return index
    #     start_node = data['nodes'][start_node][instruction_map[instruction]]
    # return -1
    cycle_instructions = cycle(data['instructions'])
    steps = 0
    while start_node[-1] != 'Z':
        start_node = data['nodes'][start_node][instruction_map[next(cycle_instructions)]]
        steps += 1
    return steps
