from utils import get_input
from functools import cache

input = get_input('input.txt')[0].split()

evoultion_count = 0

@cache
def evolve(n, input):

    evolution = []
    if n == 0:
        print(f"Final Evolution: {input}, \nTotal Stones: {len(input)}")
        return
    for i in input:
        if i == '0':
            evolution.append('1')
        elif len(i) % 2 == 0:
            length = len(i)
            i = list(map(str, [int("".join(i[:length//2])), int("".join(i[(length//2):]))]))
            evolution.extend(i)
        else:
            i = str(int(i) * 2024)
            evolution.append(i)
    print(f"Evolution {n}")
    evolve(n-1, tuple(evolution))

evolve(75, tuple(input))
