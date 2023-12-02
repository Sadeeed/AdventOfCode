# --- Day 2: Cube Conundrum ---
# Part 1
from utils import get_input, parse_game, get_possible_games

lines = get_input("input.txt")
games = []
for line in lines:
    games.append(parse_game(line))

possible_games = get_possible_games(games, 12, 13, 14)
sum_of_ids = sum(possible_games)
print("Sum of Possible IDs: ", sum_of_ids)
