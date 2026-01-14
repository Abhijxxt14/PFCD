# Question 17
# Using the sets {'red', 'green', 'blue'} and {'cyan', 'green', 'blue', 'magenta', 'red'}, 
# display the results of:
# a) comparing the sets using each of the mathematical set operators.

# Define the sets
set1 = {'red', 'green', 'blue'}
set2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

print("Set 1:", set1)
print("Set 2:", set2)
print()
print("="*60)

# Union (|) - All elements from both sets
print("1. Union (set1 | set2):")
result = set1 | set2
print(f"   {result}")
print("   All unique elements from both sets")
print()

# Intersection (&) - Common elements in both sets
print("2. Intersection (set1 & set2):")
result = set1 & set2
print(f"   {result}")
print("   Elements present in both sets")
print()

# Difference (-) - Elements in first set but not in second
print("3. Difference (set1 - set2):")
result = set1 - set2
print(f"   {result}")
print("   Elements in set1 but not in set2")
print()

# Difference (reverse) - Elements in second set but not in first
print("4. Difference (set2 - set1):")
result = set2 - set1
print(f"   {result}")
print("   Elements in set2 but not in set1")
print()

# Symmetric Difference (^) - Elements in either set but not in both
print("5. Symmetric Difference (set1 ^ set2):")
result = set1 ^ set2
print(f"   {result}")
print("   Elements in either set but not in both")
print()

# Subset test
print("6. Is set1 a subset of set2? (set1 <= set2):")
result = set1 <= set2
print(f"   {result}")
print()

# Superset test
print("7. Is set2 a superset of set1? (set2 >= set1):")
result = set2 >= set1
print(f"   {result}")
print()

# Disjoint test
print("8. Are set1 and set2 disjoint? (set1.isdisjoint(set2)):")
result = set1.isdisjoint(set2)
print(f"   {result}")
print("   (Disjoint means they have no common elements)")
