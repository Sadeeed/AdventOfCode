# --- Day 4: Scratchcards ---
# Part 1

from utils import get_input, parse_cards

lines = get_input("input.txt")

scores, _ = parse_cards(lines)

print(f"Total Score: {sum(scores)}")
