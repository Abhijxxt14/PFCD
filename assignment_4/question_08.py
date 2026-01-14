# Question 8
# Write a function that takes n as an input and creates a list of n lists such that 
# i^th list contains the first five multiples of i.

def create_multiples_list(n):
    result = []
    for i in range(1, n + 1):
        multiples = [i * j for j in range(1, 6)]
        result.append(multiples)
    return result

# Test
n = int(input("Enter the value of n: "))
result = create_multiples_list(n)

print(f"\nList of {n} lists:")
for i, lst in enumerate(result, 1):
    print(f"List {i} (multiples of {i}): {lst}")
