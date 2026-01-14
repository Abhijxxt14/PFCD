# Question 16
# Given the sets {10, 20, 30} and {5, 10, 15, 20}, use the mathematical set operators 
# to produce the following sets:
# a) {30}
# b) {5, 15, 30}
# c) {5, 10, 15, 20, 30}
# d) {10, 20}

# Define the sets
set1 = {10, 20, 30}
set2 = {5, 10, 15, 20}

print("Set 1:", set1)
print("Set 2:", set2)
print()

# a) {30} - Elements in set1 but not in set2 (set difference)
result_a = set1 - set2
print(f"a) set1 - set2 = {result_a}")
print(f"   (Elements in set1 but not in set2)")
print()

# b) {5, 15, 30} - Symmetric difference (elements in either set but not in both)
result_b = set1 ^ set2
print(f"b) set1 ^ set2 = {result_b}")
print(f"   (Symmetric difference - elements in either set but not in both)")
print()

# c) {5, 10, 15, 20, 30} - Union (all elements from both sets)
result_c = set1 | set2
print(f"c) set1 | set2 = {result_c}")
print(f"   (Union - all elements from both sets)")
print()

# d) {10, 20} - Intersection (common elements in both sets)
result_d = set1 & set2
print(f"d) set1 & set2 = {result_d}")
print(f"   (Intersection - common elements in both sets)")
