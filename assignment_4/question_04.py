# Question 4
# Write a Python program that removes all occurrences of a specific element from a list.

def remove_all_occurrences(lst, element):
    while element in lst:
        lst.remove(element)
    return lst

# Test
my_list = [1, 2, 3, 4, 2, 5, 2, 6, 2]
print(f"Original list: {my_list}")

element_to_remove = int(input("Enter the element to remove: "))
result = remove_all_occurrences(my_list.copy(), element_to_remove)

print(f"List after removing all occurrences of {element_to_remove}: {result}")
