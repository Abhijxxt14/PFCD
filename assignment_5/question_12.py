# Question 12
# Write a program that uses a dictionary to determine and print the number of duplicate 
# words in a sentence. Treat uppercase and lowercase letters the same and assume there is 
# no punctuation in the sentence.

def count_duplicate_words(sentence):
    # Convert to lowercase and split into words
    words = sentence.lower().split()
    
    # Count occurrences of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Find duplicate words
    duplicates = {word: count for word, count in word_count.items() if count > 1}
    
    return word_count, duplicates

# Test
sentence = input("Enter a sentence: ")

word_count, duplicates = count_duplicate_words(sentence)

print(f"\nSentence: '{sentence}'")
print(f"\nWord counts: {word_count}")

if duplicates:
    print(f"\nDuplicate words found: {len(duplicates)}")
    for word, count in duplicates.items():
        print(f"  '{word}' appears {count} times")
else:
    print("\nNo duplicate words found!")
