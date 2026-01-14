# Question 19
# Write a Python function to demonstrate the difference between shallow and deep copy of lists.
# Example:
# Original List: [['Shallow', 2, 3], [4, 5, 6]]
# Shallow Copy: [['Shallow', 2, 3], [4, 5, 6]]
# Deep Copy: [[1, 2, 3], ['Deep', 5, 6]]

import copy

def demonstrate_copy_difference():
    # Original list with nested lists
    original_list = [[1, 2, 3], [4, 5, 6]]
    print(f"Original List: {original_list}")
    
    # Shallow copy
    shallow_copy = original_list.copy()
    # or shallow_copy = original_list[:]
    # or shallow_copy = list(original_list)
    
    # Deep copy
    deep_copy = copy.deepcopy(original_list)
    
    # Modify the original list
    original_list[0][0] = 'Shallow'
    original_list[1][1] = 'Deep'
    
    print(f"\nAfter modifying original list:")
    print(f"Original List: {original_list}")
    print(f"Shallow Copy: {shallow_copy}")  # Shows changes because it shares nested objects
    print(f"Deep Copy: {deep_copy}")  # No changes because it's completely independent
    
    print("\n--- Detailed Explanation ---")
    print("Shallow Copy: Copies the outer list but inner lists are still references.")
    print("             Modifying nested elements affects both original and shallow copy.")
    print("Deep Copy:    Creates completely independent copy of all nested structures.")
    print("             Modifying nested elements only affects the original.")

# Run demonstration
demonstrate_copy_difference()
