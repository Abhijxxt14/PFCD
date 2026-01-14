# Question 16
# Write a Python program that prompts the user to enter a list and displays whether 
# the list is sorted or not. Here is a sample run. Note that the first number in the 
# input indicates the number of elements in the list. This number is not part of the list.
# Sample runs:
# Enter list: 8 10 1 5 16 61 9 11 1
# The list is not sorted
# Enter list: 10 1 1 3 4 4 5 7 9 11 21
# The list is already sorted

def is_sorted(lst):
    return lst == sorted(lst)

# Input
input_str = input("Enter list: ")
numbers = list(map(int, input_str.split()))

# First number is the count, rest is the list
count = numbers[0]
actual_list = numbers[1:count+1]

# Check if sorted
if is_sorted(actual_list):
    print("The list is already sorted")
else:
    print("The list is not sorted")
