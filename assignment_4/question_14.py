# Question 14
# Write a Python program that generates a tuple where each element is the square 
# of an integer from 1 to n.

def generate_square_tuple(n):
    return tuple(i**2 for i in range(1, n+1))

# Test
n = int(input("Enter the value of n: "))
result = generate_square_tuple(n)

print(f"Tuple of squares from 1 to {n}: {result}")
