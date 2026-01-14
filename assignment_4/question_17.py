# Question 17
# You can compute the standard deviation with the following formula: 
# you have to store the individual numbers using a list so that they can be used 
# after the mean is obtained.
#
# mean = (Σ xi) / n = (x1 + x2 + x3 + ... + xn) / n
# deviation = sqrt((Σ(xi - mean)²) / (n - 1))
#
# Write a Python program that prompts the user to enter ten numbers and displays 
# the mean and standard deviation.
# Sample run:
# Enter ten numbers: 1 9 2 5 3 7 2 1 6 3 4 5 2
# The mean is 3.11
# The standard deviation is 1.55738.

import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    return math.sqrt(variance)

# Input
input_str = input("Enter ten numbers: ")
numbers = list(map(float, input_str.split()))

# Calculate mean and standard deviation
mean = calculate_mean(numbers)
std_dev = calculate_standard_deviation(numbers)

print(f"The mean is {mean:.2f}")
print(f"The standard deviation is {std_dev:.5f}")
