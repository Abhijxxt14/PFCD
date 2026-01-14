# Question 10
# Write a program to find the number of occurrences of each vowel present in a given string, 
# and also print the vowels.

def count_vowel_occurrences(s):
    vowels = 'aeiouAEIOU'
    vowel_count = {}
    
    for char in s:
        if char in vowels:
            char_lower = char.lower()
            if char_lower in vowel_count:
                vowel_count[char_lower] += 1
            else:
                vowel_count[char_lower] = 1
    
    return vowel_count

# Test
test_string = input("Enter a string: ")
result = count_vowel_occurrences(test_string)

print(f"\nString: '{test_string}'")
print(f"Vowel occurrences: {result}")
print()

if result:
    print("Vowels found:")
    for vowel, count in sorted(result.items()):
        print(f"  '{vowel}': {count} time(s)")
else:
    print("No vowels found in the string!")
