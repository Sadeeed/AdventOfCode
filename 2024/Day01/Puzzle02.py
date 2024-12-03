from utils import get_input
from collections import Counter

input = get_input('input.txt')
col1 = []
col2 = []

# split all elements of input by "  " and append to col1 and col2 accordingly

for elem in input:
    split_elm = elem.split("  ")
    col1.append(int(split_elm[0].replace(" ", "")))
    col2.append(int(split_elm[1].replace(" ", "")))

# col1.sort()
# col2.sort()

# print(col1)
# print(col2)

counts = Counter(col2)
print(counts)

similarity_scores = []

for elem in col1:
    similarity_score = elem * counts.get(elem, 0)
    similarity_scores.append(similarity_score)

print(similarity_scores)
total = sum(similarity_scores)
print(total)



