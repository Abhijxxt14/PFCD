# Question 3
# Write a program to take a user-input dictionary and print the sum of the values.

def sum_dictionary_values():
    my_dict = {}
    
    n = int(input("Enter number of key-value pairs: "))
    
    for i in range(n):
        key = input(f"Enter key {i+1}: ")
        value = float(input(f"Enter value for '{key}': "))
        my_dict[key] = value
    
    print(f"\nDictionary: {my_dict}")
    
    total = sum(my_dict.values())
    print(f"Sum of all values: {total}")

# Run the program
sum_dictionary_values()
