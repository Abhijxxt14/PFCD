# Question 22
# When combining filter and map operations, the order in which they're performed matters. 
# Consider a list numbers containing 10, 3, 7, 1, 9, 4, 2, 8, 5, 6 and the following code:
# In [1]: numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
# In [2]: list(map(lambda x: x * 2,
#         ... filter(lambda x: x % 2 == 0, numbers)))
# ...
# Out[3]: [20, 8, 4, 16, 12]
# Reorder this code to call map first and filter second. What happens and why?

print("Question 22: Order of filter and map operations")
print("=" * 70)

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

print(f"Original list: {numbers}")
print()

# Original order: filter first, then map
print("Original order: Filter THEN Map")
print("Code: list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))")
result1 = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Step 1 - Filter even numbers: {list(filter(lambda x: x % 2 == 0, numbers))}")
print(f"Step 2 - Multiply by 2: {result1}")
print()

# Reversed order: map first, then filter
print("Reversed order: Map THEN Filter")
print("Code: list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers)))")
result2 = list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers)))
print(f"Step 1 - Multiply all by 2: {list(map(lambda x: x * 2, numbers))}")
print(f"Step 2 - Filter even numbers: {result2}")
print()

print("What happens and why?")
print("-" * 70)
print("When map is applied first:")
print("  1. All numbers are multiplied by 2: [20, 6, 14, 2, 18, 8, 4, 16, 10, 12]")
print("  2. Since multiplying any number by 2 makes it even, ALL numbers become even")
print("  3. Filter keeps all of them (all are even)")
print(f"  4. Result: {result2}")
print()
print("When filter is applied first:")
print("  1. Only even numbers are kept: [10, 4, 2, 8, 6]")
print("  2. Then these are multiplied by 2")
print(f"  3. Result: {result1}")
print()
print("Conclusion: The order matters significantly!")
print("  - Filter first = fewer operations (more efficient)")
print("  - Map first = all numbers doubled, then all pass the even filter")
