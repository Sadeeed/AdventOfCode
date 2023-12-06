from utils import get_input, parse_with_kerning, get_winning_distances

lines = get_input('input.txt')

data = parse_with_kerning(lines)

winning_distances = get_winning_distances(data)
print(winning_distances)

distance_product = 1
for key, value in winning_distances.items():
    print(f'Time: {key} | Ways To Win: {len(value)}')
    distance_product *= len(value)

print(f'Product of winning distances: {distance_product}')
