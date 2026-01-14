# Question 11
# Write a Python program to print M-by-N list in the tabular format.

def print_tabular_format(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:8}", end="")
        print()

# Test
m = int(input("Enter number of rows (M): "))
n = int(input("Enter number of columns (N): "))

matrix = []
print(f"\nEnter the {m}x{n} matrix:")
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

print(f"\nMatrix in tabular format:")
print_tabular_format(matrix)
