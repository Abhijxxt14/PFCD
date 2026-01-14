# Question 6
# For the following dictionary, create lists of its keys, values, and items, 
# and show those lists.
# roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}

# Create the dictionary
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}

print("Original Dictionary:")
print(roman_numerals)
print()

# Create list of keys
keys_list = list(roman_numerals.keys())
print("List of keys:")
print(keys_list)
print()

# Create list of values
values_list = list(roman_numerals.values())
print("List of values:")
print(values_list)
print()

# Create list of items (key-value pairs as tuples)
items_list = list(roman_numerals.items())
print("List of items:")
print(items_list)
