# Question 9
# Given the following inputs, indicate in each case (1) to (16), whether the statements 
# will execute successfully. If so, give what will be the outcome of execution?

address = 'B-6, Lodhi road, Delhi'
list1 = [1, 2, 3]
list2 = ['a', 1, '.', '26', 'd', 4]
tuple1 = ('a', 'c', 'T', 'o', 'u')
tuple2 = ([2,4,6,8], [3,6,9], [4,8], 5)

print("1. list1[3] = 4")
try:
    list1[3] = 4
    print(f"   Success! list1 = {list1}")
except Exception as e:
    print(f"   Error: {type(e).__name__}: {e}")

print("\n2. print(list1 * 2)")
try:
    result = list1 * 2
    print(f"   Output: {result}")
except Exception as e:
    print(f"   Error: {type(e).__name__}: {e}")

print("\n3. print(min(list2))")
try:
    result = min(list2)
    print(f"   Output: {result}")
except Exception as e:
    print(f"   Error: {type(e).__name__}: {e}")

print("\n4. print(max(list1))")
try:
    result = max(list1)
    print(f"   Output: {result}")
except Exception as e:
    print(f"   Error: {type(e).__name__}: {e}")

print("\n5. print(list(address))")
try:
    result = list(address)
    print(f"   Output: {result}")
except Exception as e:
    print(f"   Error: {type(e).__name__}: {e}")

print("\n6. list2.extend(['e', 5])")
try:
    list2_copy = list2.copy()
    list2_copy.extend(['e', 5])
    print(f"   Output: {list2_copy}")
except Exception as e:
    print(f"   Error: {type(e).__name__}: {e}")

print("\n7. list2.append(['e', 5])")
try:
    list2_copy = list2.copy()
    list2_copy.append(['e', 5])
    print(f"   Output: {list2_copy}")
except Exception as e:
    print(f"   Error: {type(e).__name__}: {e}")

print("\n8. names = ['rohan', 'mohan', 'gita']")
print("   names.sort(key=len)")
try:
    names = ['rohan', 'mohan', 'gita']
    names.sort(key=len)
    print(f"   Output: {names}")
except Exception as e:
    print(f"   Error: {type(e).__name__}: {e}")

print("\n9. list3 = [(x * 2) for x in range(1, 11)]")
try:
    list3 = [(x * 2) for x in range(1, 11)]
    print(f"   Output: {list3}")
except Exception as e:
    print(f"   Error: {type(e).__name__}: {e}")

print("\n10. del list3[1:]")
try:
    del list3[1:]
    print(f"    Output: {list3}")
except Exception as e:
    print(f"    Error: {type(e).__name__}: {e}")

print("\n11. list4 = [x+y for x in range(1,5) for y in range(1,5)]")
try:
    list4 = [x+y for x in range(1,5) for y in range(1,5)]
    print(f"    Output: {list4}")
except Exception as e:
    print(f"    Error: {type(e).__name__}: {e}")

print("\n12. tuple2[3] = 6")
try:
    tuple2[3] = 6
    print(f"    Output: {tuple2}")
except Exception as e:
    print(f"    Error: {type(e).__name__}: {e}")

print("\n13. tuple2.append(5)")
try:
    tuple2.append(5)
    print(f"    Output: {tuple2}")
except Exception as e:
    print(f"    Error: {type(e).__name__}: {e}")

print("\n14. t1 = tuple2 + (5)")
try:
    t1 = tuple2 + (5)
    print(f"    Output: {t1}")
except Exception as e:
    print(f"    Error: {type(e).__name__}: {e}")

print("\n15. ', '.join(tuple1)")
try:
    result = ', '.join(tuple1)
    print(f"    Output: {result}")
except Exception as e:
    print(f"    Error: {type(e).__name__}: {e}")

print("\n16. list(zip(['apple', 'orange'], ('red','orange')))")
try:
    result = list(zip(['apple', 'orange'], ('red','orange')))
    print(f"    Output: {result}")
except Exception as e:
    print(f"    Error: {type(e).__name__}: {e}")
