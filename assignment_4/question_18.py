# Question 18
# Write a Python program to create a new list that contains the square of every 
# element in a given list using list comprehension.

def square_elements(lst):
    return [x**2 for x in lst]

# Test
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {original_list}")

squared_list = square_elements(original_list)
print(f"Squared list: {squared_list}")

# Another test with user input
n = int(input("\nEnter number of elements: "))
user_list = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    user_list.append(num)

print(f"Original list: {user_list}")
print(f"Squared list: {square_elements(user_list)}")
