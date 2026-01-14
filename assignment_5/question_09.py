# Question 9
# Write a program to find the number of occurrences of each letter present in a given string, 
# e.g., str='mississippi' => {'m': 1, 'i': 4, 's': 4, 'p': 2}

def count_letter_occurrences(s):
    letter_count = {}
    
    for char in s:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    
    return letter_count

# Test with the example
test_string = 'mississippi'
print(f"String: '{test_string}'")
result = count_letter_occurrences(test_string)
print(f"Letter occurrences: {result}")
print()

# Test with user input
user_input = input("Enter a string: ")
result = count_letter_occurrences(user_input)
print(f"Letter occurrences: {result}")
