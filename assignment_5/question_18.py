# Question 18
# You are given two lists of integers: list1 and list2. Write a Python function 
# analyze_sets(list1, list2) that performs the following tasks:
#
# • Creates two sets, set1 and set2, from list1 and list2.
# • Finds the symmetric difference of set1 and set2 (elements that are in either set 
#   but not in both).
# • For each element in the symmetric difference:
#   - If the element is even, multiply it by 2.
#   - If the element is odd, add 5 to it.
# • Return a sorted list of the modified elements.

def analyze_sets(list1, list2):
    # Create sets from the lists
    set1 = set(list1)
    set2 = set(list2)
    
    print(f"Set 1 (from list1): {set1}")
    print(f"Set 2 (from list2): {set2}")
    
    # Find symmetric difference
    symmetric_diff = set1 ^ set2
    print(f"Symmetric difference: {symmetric_diff}")
    
    # Modify elements based on even/odd
    modified_elements = []
    for element in symmetric_diff:
        if element % 2 == 0:
            # Even: multiply by 2
            modified_elements.append(element * 2)
        else:
            # Odd: add 5
            modified_elements.append(element + 5)
    
    # Return sorted list
    return sorted(modified_elements)

# Test
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

print("List 1:", list1)
print("List 2:", list2)
print()

result = analyze_sets(list1, list2)

print(f"\nFinal result (sorted modified elements): {result}")
print()

# Show the transformation process
print("Transformation details:")
set1 = set(list1)
set2 = set(list2)
symmetric_diff = set1 ^ set2
for element in sorted(symmetric_diff):
    if element % 2 == 0:
        print(f"  {element} is even -> multiply by 2 -> {element * 2}")
    else:
        print(f"  {element} is odd -> add 5 -> {element + 5}")
