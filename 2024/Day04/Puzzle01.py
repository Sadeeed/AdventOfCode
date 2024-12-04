from utils import get_input
import re

input = get_input('test_input.txt') # rows

def get_columns(input):
    columns = []
    for row in input:
        for i, char in enumerate(row):
            if len(columns) <= i:
                columns.append(char)
            else:
                columns[i] += char
    return columns

def get_diagonals(input):
    diagonals = []
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if len(diagonals) <= i + j:
                diagonals.append(char)
            else:
                diagonals[i + j] += char
    return diagonals

columns = get_columns(input)
diagonals = get_diagonals(input)

total = 0

print("Rows\n")
for row in input:
    row_results = re.findall(r'XMAS', row)
    row_results_i = re.findall(r'XMAS', row[::-1])
    # row_results_i = re.findall(r'SAMX', row)
    print(f"Row results: {row_results}")
    print(f"Row results_i: {row_results_i}")
    # print(f"Row results: {row_results}")
    total += len(row_results) + len(row_results_i)
    print(row)
    print(row[::-1])
print("\n************\n")



print("Columns\n")
for column in columns:
    column_results = re.findall(r'XMAS', column)
    column_results_i = re.findall(r'XMAS', column[::-1])
    # column_results_i = re.findall(r'SAMX', column)
    # print(f"Column results: {column_results}")
    total += len(column_results) + len(column_results_i)
    print(column)
print("\n************\n")


print("Diagonals\n")
for diagonal in diagonals:
    diagonal_results = re.findall(r'XMAS', diagonal)
    diagonal_results_i = re.findall(r'XMAS', diagonal[::-1])
    # diagonal_results_i = re.findall(r'SAMX', diagonal)
    # print(f"Diagonal results: {diagonal_results}")
    total += len(diagonal_results) + len(diagonal_results_i)
    print(diagonal)
print("\n************")

print(f"Total: {total}")
