# Question 1
# Write a Python program to create a list of size N and store the random values in it 
# and find the sum and average.

import random

def create_random_list(n):
    random_list = [random.randint(1, 100) for _ in range(n)]
    total_sum = sum(random_list)
    average = total_sum / n if n > 0 else 0
    return random_list, total_sum, average

# Test
n = int(input("Enter the size of the list: "))
random_list, total_sum, average = create_random_list(n)

print(f"Random list: {random_list}")
print(f"Sum: {total_sum}")
print(f"Average: {average}")
