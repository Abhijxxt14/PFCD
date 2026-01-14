# Question 19
# Given a long list of words, write a Python function unique_pairs(words) to find all 
# unique pairs of words that:
#
# • Have no common letters (e.g., "cat" and "dogs" have no letters in common).
# • Each word in the pair should have at least 4 letters.
# • Each unique pair should be stored in a set as a tuple in lexicographical order.
#
# The function should return a set of all such unique pairs.
#
# Example:
# words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
# print(unique_pairs(words))
#
# Expected Output (Order may vary due to set properties):
# {("apple", "dogs"), ("apple", "bird"), ("apple", "fish"),
#  ("bird", "dogs"), ("dogs", "fish"), ("dogs", "zebra"),
#  ("dogs", "lion"), ("fish", "zebra"), ("lion", "zebra")}

def unique_pairs(words):
    # Filter words with at least 4 letters
    valid_words = [word for word in words if len(word) >= 4]
    
    # Create a set to store unique pairs
    unique_pairs_set = set()
    
    # Check all pairs of words
    for i in range(len(valid_words)):
        for j in range(i + 1, len(valid_words)):
            word1 = valid_words[i]
            word2 = valid_words[j]
            
            # Convert words to sets of characters
            set1 = set(word1.lower())
            set2 = set(word2.lower())
            
            # Check if they have no common letters
            if set1.isdisjoint(set2):
                # Store in lexicographical order
                pair = tuple(sorted([word1, word2]))
                unique_pairs_set.add(pair)
    
    return unique_pairs_set

# Test with the example
words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]

print(f"Words: {words}")
print()

result = unique_pairs(words)

print(f"Unique pairs with no common letters:")
for pair in sorted(result):
    word1, word2 = pair
    print(f"  {pair}")
    print(f"    '{word1}' has letters: {set(word1)}")
    print(f"    '{word2}' has letters: {set(word2)}")
    print(f"    Common letters: {set(word1) & set(word2)} (none)")
    print()

print(f"\nTotal unique pairs: {len(result)}")
print(f"\nResult set: {result}")
