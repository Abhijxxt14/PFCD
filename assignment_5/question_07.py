# Question 7
# Use dictionary comprehension to create a dictionary of the numbers 1-5 mapped to their cubes.

# Create dictionary using dictionary comprehension
cubes_dict = {num: num**3 for num in range(1, 6)}

print("Dictionary of numbers 1-5 mapped to their cubes:")
print(cubes_dict)
print()

# Display in formatted way
print("Number -> Cube")
print("-" * 20)
for num, cube in cubes_dict.items():
    print(f"{num:^6} -> {cube:^6}")
