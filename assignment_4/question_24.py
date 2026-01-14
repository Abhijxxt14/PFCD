# Question 24
# Given a list of tuples, remove all the tuples with length K, where K is user-defined.

def remove_tuples_with_length_k(tuple_list, k):
    return [t for t in tuple_list if len(t) != k]

# Test
test_list = [
    (1, 2),
    (3, 4, 5),
    (6, 7),
    (8, 9, 10, 11),
    (12,),
    (13, 14, 15)
]

print(f"Original list of tuples: {test_list}")

k = int(input("\nEnter the length K to remove: "))

result = remove_tuples_with_length_k(test_list, k)

print(f"List after removing tuples with length {k}: {result}")
