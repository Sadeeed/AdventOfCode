from utils import get_input
from functools import cache
from collections import Counter

input = Counter(get_input("test_input2.txt")[0].split())

def evolve(n, input):
    evolution = Counter()
    if n == 0:
        print(f"Final Evolution: {input.keys()}, \nTotal Stones: {sum(input.values())}")
        return
    for i in input:
        if i == "0":
            evolution[i] += evolution.get(i, input[i]) + 1
        elif len(i) % 2 == 0:
            length = len(i)
            left_stone, right_stone = list(
                map(
                    str,
                    [int("".join(i[: length // 2])), int("".join(i[(length // 2) :]))],
                )
            )
            # evolution.extend(i)
            # print(f"Left Stone: {left_stone}, Right Stone: {right_stone}")
            evolution[left_stone] = evolution.get(left_stone, input[i]) + 1
            evolution[right_stone] = evolution.get(right_stone, input[i]) + 1
        else:
            # i = str(int(i) * 2024)
            # evolution.append(i)
            evolution[str(int(i) * 2024)] = evolution.get(str(int(i) * 2024), input[i]) + 1
    print(f"Evolution {n}")
    evolve(n - 1, evolution)


evolve(6, input)
