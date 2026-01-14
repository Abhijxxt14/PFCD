# Question 14
# Create a program that determines and displays the number of unique characters in a string 
# entered by the user, e.g., 'Hello, World!' has 10 unique characters, while 'zzz' has only 
# one unique character. Use a set or dictionary to solve this problem.

def count_unique_characters(s):
    # Using set to get unique characters
    unique_chars = set(s)
    
    return unique_chars, len(unique_chars)

# Test with examples
test_strings = ["Hello, World!", "zzz", "aabbcc", "Python Programming"]

for test in test_strings:
    unique_chars, count = count_unique_characters(test)
    print(f"String: '{test}'")
    print(f"Unique characters: {sorted(unique_chars)}")
    print(f"Number of unique characters: {count}")
    print()

# User input
user_input = input("Enter a string: ")
unique_chars, count = count_unique_characters(user_input)

print(f"\nString: '{user_input}'")
print(f"Unique characters: {sorted(unique_chars)}")
print(f"Number of unique characters: {count}")
