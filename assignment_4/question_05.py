# Question 5
# Are there any mistakes in these codes? State the outputs:

print("a) day, high_temperature = ('Monday', 87, 65)")
print("   Mistake: Too many values to unpack. Tuple has 3 values but only 2 variables.")
print("   Error: ValueError: too many values to unpack (expected 2)")
print()

print("b) numbers = [1, 2, 3, 4, 5]")
print("   numbers[10]")
print("   Mistake: Index out of range. List has only 5 elements (indices 0-4).")
print("   Error: IndexError: list index out of range")
print()

print("c) name = 'amanda'")
print("   name[0] = 'A'")
print("   Mistake: Strings are immutable in Python. Cannot modify individual characters.")
print("   Error: TypeError: 'str' object does not support item assignment")
print()

print("d) numbers = [1, 2, 3, 4, 5]")
print("   numbers[3:4]")
print("   Mistake: No mistake. This is valid slicing.")
print("   Output: [4]")
print()

print("e) student_tuple = ('Amanda', 'Blue', [98, 75, 87])")
print("   student_tuple[0] = 'Ariana'")
print("   Mistake: Tuples are immutable. Cannot modify elements.")
print("   Error: TypeError: 'tuple' object does not support item assignment")
print()

print("f) ('Monday', 87, 65) + 'Tuesday'")
print("   Mistake: Cannot concatenate tuple with string.")
print("   Error: TypeError: can only concatenate tuple (not 'str') to tuple")
print()

print("g) 'A' += ('B', 'C')")
print("   Mistake: Cannot concatenate string with tuple.")
print("   Error: TypeError: can only concatenate str (not 'tuple') to str")
print()

print("h) x = 7")
print("   del x")
print("   print(x)")
print("   Mistake: Variable x is deleted, so it doesn't exist when trying to print.")
print("   Error: NameError: name 'x' is not defined")
print()

print("i) numbers = [1, 2, 3, 4, 5]")
print("   numbers.index(10)")
print("   Mistake: 10 is not in the list.")
print("   Error: ValueError: 10 is not in list")
print()

print("j) numbers = [1, 2, 3, 4, 5]")
print("   numbers.extend(6, 7, 8)")
print("   Mistake: extend() takes exactly one argument (an iterable).")
print("   Error: TypeError: extend() takes exactly one argument (3 given)")
print("   Correct: numbers.extend([6, 7, 8])")
print()

print("k) numbers = [1, 2, 3, 4, 5]")
print("   numbers.remove(10)")
print("   Mistake: 10 is not in the list.")
print("   Error: ValueError: list.remove(x): x not in list")
print()

print("l) values = []")
print("   values.pop()")
print("   Mistake: Cannot pop from an empty list.")
print("   Error: IndexError: pop from empty list")
