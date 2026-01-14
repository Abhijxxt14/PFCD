# Question 7
# Write a function that takes a list of numbers as input from the user and produces 
# the corresponding cumulative list where each element in the list at index i is 
# the sum of elements at index j ≤ i.

def cumulative_list(numbers):
    cumulative = []
    total = 0
    for num in numbers:
        total += num
        cumulative.append(total)
    return cumulative

# Test
n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(f"\nOriginal list: {numbers}")

result = cumulative_list(numbers)
print(f"Cumulative list: {result}")
