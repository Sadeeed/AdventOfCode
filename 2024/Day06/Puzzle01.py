from utils import get_input

input = get_input('test_input.txt')

def get_starting_index(input):
    for i in range(len(input)):
        row = input[i]
        for j in range(len(row)):
            if row[j] == '^':
                return i, j
    return 0, 0

starting_index = get_starting_index(input)
row_length = len(input[0])
column_length = len(input)
