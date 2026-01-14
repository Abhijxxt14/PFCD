# Question 13
# Write a Python function that sorts a list of tuples based on the second element of each tuple.

def sort_by_second_element(tuple_list):
    return sorted(tuple_list, key=lambda x: x[1])

# Test
test_list = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1), ('elderberry', 4)]
print(f"Original list: {test_list}")

sorted_list = sort_by_second_element(test_list)
print(f"Sorted list (by second element): {sorted_list}")
