from utils import get_input

input = get_input('input.txt')
col1 = []
col2 = []

# split all elements of input by "  " and append to col1 and col2 accordingly

for elem in input:
    split_elm = elem.split("  ")
    col1.append(int(split_elm[0].replace(" ", "")))
    col2.append(int(split_elm[1].replace(" ", "")))

print(col1)
print(col2)

col1.sort()
col2.sort()

print(col1)
print(col2)

distance = []

for a,b in zip(col1, col2):
    distance.append(abs(a-b))

print(distance)
total_distance = sum(distance)
print(total_distance)
