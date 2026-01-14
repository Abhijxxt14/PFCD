# Question 13
# Write a function that receives a list of words, then determines and displays in alphabetical 
# order only the unique words. Also, display uppercase and lowercase words separately and 
# get the unique words in the list. Test your function with several sentences.

def analyze_words(words_list):
    # Get unique words
    unique_words = list(set(words_list))
    
    # Sort alphabetically
    unique_words_sorted = sorted(unique_words, key=str.lower)
    
    # Separate uppercase and lowercase words
    uppercase_words = sorted([word for word in unique_words if word[0].isupper()])
    lowercase_words = sorted([word for word in unique_words if word[0].islower()])
    
    return unique_words_sorted, uppercase_words, lowercase_words

# Test
sentence = input("Enter a sentence: ")
words = sentence.split()

print(f"\nOriginal words: {words}")

unique_sorted, uppercase, lowercase = analyze_words(words)

print(f"\nUnique words (alphabetical order): {unique_sorted}")
print(f"Uppercase words: {uppercase}")
print(f"Lowercase words: {lowercase}")

# Test with more sentences
print("\n" + "="*50)
print("Testing with multiple sentences:")
print("="*50)

test_sentences = [
    "The quick brown Fox jumps over the lazy Dog",
    "Python Python python PYTHON",
    "Hello World Hello world HELLO"
]

for sent in test_sentences:
    words = sent.split()
    unique_sorted, uppercase, lowercase = analyze_words(words)
    print(f"\nSentence: '{sent}'")
    print(f"Unique words: {unique_sorted}")
    print(f"Uppercase: {uppercase}")
    print(f"Lowercase: {lowercase}")
