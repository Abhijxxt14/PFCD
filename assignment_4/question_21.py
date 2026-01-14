# Question 21
# With regard to the following code:
# numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
# list(filter(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
# 
# a) How many times does the filter operation call its lambda argument?
# b) How many times does the map operation call its lambda argument?
# c) If you reverse the filter and map operations, how many times does the map operation 
#    call its lambda argument?

print("Question 21: Analyzing lambda calls in filter and map operations")
print("=" * 70)

# Original code analysis
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

print(f"Original list: {numbers}")
print()

# Part a) Filter operation
print("a) Filter operation: lambda x: x % 2 != 0")
print("   This filter checks if each number is odd.")
print(f"   The filter will be called {len(numbers)} times (once for each element)")
print(f"   Result: {list(filter(lambda x: x % 2 != 0, numbers))}")
print()

# Note: The original code has a mistake - filter expects a boolean, not x**2
# Let's analyze both the original and corrected versions

print("b) With map operation: map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers))")
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f"   Odd numbers after filter: {odd_numbers}")
print(f"   The map will be called {len(odd_numbers)} times")
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
print(f"   Result: {result}")
print()

print("c) Reversing filter and map operations:")
print("   map(lambda x: x ** 2, numbers) first, then filter")
squared = list(map(lambda x: x ** 2, numbers))
print(f"   After map (all squared): {squared}")
print(f"   The map will be called {len(numbers)} times (once for each element)")
print(f"   Then filter on the squared values")
print()

print("Summary:")
print(f"a) Filter lambda is called: {len(numbers)} times")
print(f"b) Map lambda is called: {len(odd_numbers)} times (only on filtered odd numbers)")
print(f"c) If reversed, map lambda is called: {len(numbers)} times (on all elements)")
