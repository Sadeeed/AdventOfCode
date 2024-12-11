from utils import get_input
from functools import cache
from collections import Counter

input = Counter(get_input("input.txt")[0].split())

def evolve(n, input):
    evolution = Counter()
    if n == 0:
        print(f"Final Evolution: {input}, \nTotal Stones: {sum(input.values())}")
        return
    for i in input:
        if i == "0":
            evolution['1'] = evolution.get('1', 0) + input[i]
        elif len(i) % 2 == 0:
            length = len(i)
            left_stone, right_stone = list(
                map(
                    str,
                    [int("".join(i[: length // 2])), int("".join(i[(length // 2) :]))],
                )
            )
            # print(f"Left Stone: {left_stone}, Right Stone: {right_stone}")
            evolution[left_stone] = evolution.get(left_stone, 0) + input[i]
            evolution[right_stone] = evolution.get(right_stone, 0) + input[i]
        else:
            evolution[str(int(i) * 2024)] = evolution.get(str(int(i) * 2024), 0) + input[i]
    print(f"Evolution {n}: {evolution}\n")
    evolve(n - 1, evolution)

evolve(75, input)
