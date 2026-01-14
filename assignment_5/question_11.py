# Question 11
# Write a function that takes a number as an input parameter and returns the corresponding 
# text in words, e.g., on input 452, the function should return 'Four Five Two'. 
# Use a dictionary for mapping digits to their word representations.

def number_to_words(number):
    digit_to_word = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    
    # Convert number to string and map each digit
    words = [digit_to_word[digit] for digit in str(abs(number))]
    
    return ' '.join(words)

# Test
test_numbers = [452, 123, 9876, 0, 5]

for num in test_numbers:
    print(f"{num} -> '{number_to_words(num)}'")

print()

# User input
user_number = int(input("Enter a number: "))
print(f"{user_number} -> '{number_to_words(user_number)}'")
