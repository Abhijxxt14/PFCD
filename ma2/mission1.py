"""
Mission 1: Clearing the Field
Task: To remove duplicates from the list and sort it alphabetically
"""

def clear_field(cities):
    cleaned_cities = sorted(set(cities))
    return cleaned_cities

cities = ["Kyiv", "Kharkiv", "Odessa", "Kyiv", "Lviv", "Kharkiv", "Dnipro"]
cleaned_cities = clear_field(cities)
print("Input:", cities)
print("Output:", cleaned_cities)



"""
Expected Output:

Input: ['Kyiv', 'Kharkiv', 'Odessa', 'Kyiv', 'Lviv', 'Kharkiv', 'Dnipro']
Output: ['Dnipro', 'Kharkiv', 'Kyiv', 'Lviv', 'Odessa']
"""