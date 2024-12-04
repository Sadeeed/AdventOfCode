from utils import get_input
import re
import numpy as np

input = get_input('input.txt') # rows

def get_columns(input):
    columns = []
    for row in input:
        for i, char in enumerate(row):
            if len(columns) <= i:
                columns.append(char)
            else:
                columns[i] += char
    return columns

def get_columns_np(input):
    # list comprehension to spit each element in input to a list
    input = [list(row) for row in input]
    input = np.array(input)
    # input = np.transpose(input)
    # return [''.join(row) for row in input]
    return ["".join(input[:, i]) for i in range(input.shape[1])]


def get_diagonals(input):
    diagonals = []
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if len(diagonals) <= i + j:
                diagonals.append(char)
            else:
                diagonals[i + j] += char
    return diagonals


def get_diagonals_np(input):
    # list comprehension to spit each element in input to a list
    input = [list(row) for row in input]
    input = np.array(input)

    list_ = [input[::-1,:].diagonal(i) for i in range(-input.shape[0]+1,input.shape[1])]
    list_.extend(input.diagonal(i) for i in range(input.shape[1]-1,-input.shape[0],-1))

    # input = np.flipud(input)
    # a = input.shape[0]
    # list_ = [np.diag(input, k=i).tolist() for i in range(-a+1,a)]
    return [''.join(row) for row in list_]

columns = get_columns(input)
# diagonals = get_diagonals(input)
diagonals = get_diagonals_np(input)



total = 0
print("Rows\n")
for row in input:
    row_results = re.findall(r'XMAS', row)
    row_results_i = re.findall(r'XMAS', row[::-1])
    # print(f"Row results: {row_results}")
    total += len(row_results) + len(row_results_i)
    print(row)
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
    total += len(diagonal_results) + len(diagonal_results_i)
    print(diagonal)
print("\n************")

print(f"Total: {total}")
