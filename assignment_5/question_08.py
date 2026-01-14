# Question 8
# Make a multilevel dictionary called life. Use these strings for the topmost keys: 
# 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with 
# the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with 
# the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.

# Create the multilevel dictionary
life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}

print("Multilevel Dictionary 'life':")
print(life)
print()

# Display in a more readable format
print("Formatted view:")
print("life")
for key1, value1 in life.items():
    print(f"  {key1}:")
    if isinstance(value1, dict):
        if value1:
            for key2, value2 in value1.items():
                print(f"    {key2}: {value2}")
        else:
            print(f"    (empty dictionary)")
print()

# Access specific values
print("Accessing specific values:")
print(f"life['animals']['cats']: {life['animals']['cats']}")
print(f"life['animals']['cats'][0]: {life['animals']['cats'][0]}")
