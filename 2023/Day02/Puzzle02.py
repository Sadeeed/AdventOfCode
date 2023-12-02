# --- Day 2: Cube Conundrum ---
# Part 2
from utils import get_input, parse_game, sum_of_powers

lines = get_input("input.txt")

games = []
for line in lines:
    games.append(parse_game(line))

sum_of_powers = sum_of_powers(games)
print("Sum of Powers: ", sum_of_powers)
