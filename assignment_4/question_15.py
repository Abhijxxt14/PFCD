# Question 15
# Write a Python program that randomly fills in 0s and 1s into a 4-by-4 matrix, 
# prints the matrix, and finds the first row and column with the most 1s.
# Sample run:
# 0011
# 0011
# 1101
# 1010
# The largest row index: 2
# The largest column index: 2

import random

def create_random_matrix():
    matrix = []
    for i in range(4):
        row = [random.randint(0, 1) for j in range(4)]
        matrix.append(row)
    return matrix

def find_largest_row(matrix):
    max_count = 0
    max_row = 0
    for i, row in enumerate(matrix):
        count = row.count(1)
        if count > max_count:
            max_count = count
            max_row = i
    return max_row

def find_largest_column(matrix):
    max_count = 0
    max_col = 0
    for col in range(4):
        count = sum(matrix[row][col] for row in range(4))
        if count > max_count:
            max_count = count
            max_col = col
    return max_col

# Main program
matrix = create_random_matrix()

print("Matrix:")
for row in matrix:
    print(''.join(map(str, row)))

largest_row = find_largest_row(matrix)
largest_col = find_largest_column(matrix)

print(f"The largest row index: {largest_row}")
print(f"The largest column index: {largest_col}")
