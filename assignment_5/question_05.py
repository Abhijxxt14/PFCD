# Question 5
# A dictionary which maps country names to Internet top-level domains (TLDs) is given as follows:
# tlds = {'Canada': '.ca', 'United States': '.us', 'Mexico': '.mx'}
# Perform the following tasks and display the results:
# a) Check whether the dictionary contains the key 'Canada'.
# b) Check whether the dictionary contains the key 'France'.
# c) Iterate through the key-value pairs and display them in two-column format.
# d) Add the key-value pair 'Sweden' and '.sw' (incorrect TLD).
# e) Update the value for the key 'Sweden' to '.se' (correct TLD).
# f) Use dictionary comprehension to reverse the keys and values.

# Initial dictionary
tlds = {'Canada': '.ca', 'United States': '.us', 'Mexico': '.mx'}

print("Original Dictionary:")
print(tlds)
print()

# a) Check whether the dictionary contains the key 'Canada'
print("a) Check whether 'Canada' is in dictionary:")
print(f"   'Canada' in tlds: {'Canada' in tlds}")
print()

# b) Check whether the dictionary contains the key 'France'
print("b) Check whether 'France' is in dictionary:")
print(f"   'France' in tlds: {'France' in tlds}")
print()

# c) Iterate through the key-value pairs and display them in two-column format
print("c) Key-value pairs in two-column format:")
print(f"   {'Country':<20} {'TLD'}")
print("   " + "-"*30)
for country, tld in tlds.items():
    print(f"   {country:<20} {tld}")
print()

# d) Add the key-value pair 'Sweden' and '.sw' (incorrect TLD)
print("d) Adding 'Sweden': '.sw' (incorrect TLD):")
tlds['Sweden'] = '.sw'
print(f"   {tlds}")
print()

# e) Update the value for the key 'Sweden' to '.se' (correct TLD)
print("e) Updating 'Sweden' to '.se' (correct TLD):")
tlds['Sweden'] = '.se'
print(f"   {tlds}")
print()

# f) Use dictionary comprehension to reverse the keys and values
print("f) Reversed dictionary (TLD to Country):")
reversed_tlds = {value: key for key, value in tlds.items()}
print(f"   {reversed_tlds}")
