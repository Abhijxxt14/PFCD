# Question 12
# Define a function that returns the sum of all the elements in a specified column in a matrix.
# Write a Python program that reads a 3-by-4 matrix and displays the sum of each column.
# Here is a sample run:
# Enter a 3-by-4 matrix row by row:
# 1.5 2 3 4
# 5.5 6 7 8
# 9.5 1 3 1

def column_sum(matrix, col_index):
    total = 0
    for row in matrix:
        total += row[col_index]
    return total

def read_matrix():
    matrix = []
    print("Enter a 3-by-4 matrix row by row:")
    for i in range(3):
        row_input = input(f"Row {i+1}: ")
        row = [float(x) for x in row_input.split()]
        matrix.append(row)
    return matrix

# Main program
matrix = read_matrix()

print("\nSum of each column:")
for col in range(4):
    col_sum = column_sum(matrix, col)
    print(f"Column {col+1}: {col_sum}")
