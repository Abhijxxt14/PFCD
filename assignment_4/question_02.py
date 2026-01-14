# Question 2
# Define a function rotate that receives three arguments and returns a tuple in which 
# the first argument is at index 2, the second argument is at index 0, and the third is at index 1.
# Create a tuple of variables a, b and c containing 'Doug', 22 and 1984. 
# Then call the function three times. For each call, unpack its result into a, b and c, 
# then display their values.

def rotate(arg1, arg2, arg3):
    return (arg2, arg3, arg1)

# Initial values
a, b, c = 'Doug', 22, 1984
print(f"Initial values: a={a}, b={b}, c={c}")

# First call
a, b, c = rotate(a, b, c)
print(f"After 1st rotation: a={a}, b={b}, c={c}")

# Second call
a, b, c = rotate(a, b, c)
print(f"After 2nd rotation: a={a}, b={b}, c={c}")

# Third call
a, b, c = rotate(a, b, c)
print(f"After 3rd rotation: a={a}, b={b}, c={c}")
