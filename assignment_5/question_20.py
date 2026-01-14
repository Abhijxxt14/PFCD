# Question 20
# Write a Python program to change Mukesh's net worth to 9650 in the following dictionary:
#
# sample_dict = {
#     'person1': {'name': 'Bezos', 'net_worth': 21,880},
#     'person2': {'name': 'Elon', 'net_worth': 31,570},
#     'person3': {'name': 'Mukesh', 'net_worth': 965}
# }

# Initial dictionary
sample_dict = {
    'person1': {'name': 'Bezos', 'net_worth': 21880},
    'person2': {'name': 'Elon', 'net_worth': 31570},
    'person3': {'name': 'Mukesh', 'net_worth': 965}
}

print("Original Dictionary:")
print(sample_dict)
print()

# Display in formatted way
print("Original Data:")
for person, info in sample_dict.items():
    print(f"  {person}: {info['name']} - Net Worth: {info['net_worth']}")
print()

# Change Mukesh's net worth to 9650
sample_dict['person3']['net_worth'] = 9650

print("Updated Dictionary:")
print(sample_dict)
print()

# Display updated data in formatted way
print("Updated Data:")
for person, info in sample_dict.items():
    print(f"  {person}: {info['name']} - Net Worth: {info['net_worth']}")
