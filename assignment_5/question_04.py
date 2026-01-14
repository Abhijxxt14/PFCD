# Question 4
# Make an English-to-French dictionary called e2f and print it. 
# Here are your starter words: dog is chien, cat is chat, and walrus is morse.

# Create the English-to-French dictionary
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

print("English-to-French Dictionary (e2f):")
print(e2f)
print()

# Display in a formatted way
print("Formatted Dictionary:")
for english, french in e2f.items():
    print(f"{english} -> {french}")
