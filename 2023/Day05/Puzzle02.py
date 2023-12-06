from utils import get_input, parse_input, get_seed_data, expand_seeds

lines = get_input('test_input.txt')

input_map = parse_input(lines)
input_map['seeds'] = expand_seeds(input_map['seeds'])
print(f"Input map: {input_map}")

seed_data = get_seed_data(input_map)
print(f"Seed data: {seed_data}")

lowest_location_seed = min(seed_data, key=lambda x: seed_data[x]['location'])
print(f"Lowest location: {seed_data[lowest_location_seed]['location']}")
