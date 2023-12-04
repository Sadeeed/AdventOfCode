# --- Day 4: Scratchcards ---
# Part 1

from utils import get_input, parse_cards, process_matches

lines = get_input("input.txt")
_, matches = parse_cards(lines)

total_cards = process_matches(matches)
print(f"Total Cards: {total_cards}")
