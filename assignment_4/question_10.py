# Question 10
# Write a Python function that takes a tuple of tuples and prints the sum of all 
# numeric elements in the inner tuples.

def sum_of_numeric_elements(tuple_of_tuples):
    total = 0
    for inner_tuple in tuple_of_tuples:
        for element in inner_tuple:
            if isinstance(element, (int, float)):
                total += element
    return total

# Test
test_tuple = ((1, 2, 3), (4, 'hello', 5), (6, 7.5, 'world', 8))
print(f"Tuple of tuples: {test_tuple}")

result = sum_of_numeric_elements(test_tuple)
print(f"Sum of all numeric elements: {result}")
