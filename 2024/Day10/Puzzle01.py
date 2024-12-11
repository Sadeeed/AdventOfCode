from utils import get_input

input = get_input('test_input.txt')

def find_trailheads(input):
    trailheads = []
    for i, row in enumerate(input):
        for c, element in enumerate(row):
            if element == '0':
                trailheads.append((i, c))

    return trailheads

theds = find_trailheads(input)
print(theds)
