"""
Mission 4: Tracking Supply Distribution
Task: To create nested dictionary to track supplies by city and type
"""

def track_supply_distribution(supplies):
    supply_tracker = {}
    
    for city, supply_type, quantity in supplies:
        if city not in supply_tracker:
            supply_tracker[city] = {}
        
        if supply_type in supply_tracker[city]:
            supply_tracker[city][supply_type] += quantity
        else:
            supply_tracker[city][supply_type] = quantity
    
    return supply_tracker

supplies = [
    ("Kyiv", "Food", 500),
    ("Moscow", "Medicines", 200),
    ("Lviv", "Water", 300),
    ("Saint Petersburg", "Blankets", 100),
    ("Kharkiv", "Food", 150)
]
    
supply_tracker = track_supply_distribution(supplies)
    
print("Input supplies:", supplies)
print("\nOutput:")
print("Supply tracker:", supply_tracker)



"""
Expected Output:

Input supplies: [('Kyiv', 'Food', 500), ('Moscow', 'Medicines', 200), ('Lviv', 'Water', 300), ('Saint Petersburg', 'Blankets', 100), ('Kharkiv', 'Food', 150)]
Output:
Supply tracker: {'Kyiv': {'Food': 500}, 'Moscow': {'Medicines': 200}, 'Lviv': {'Water': 300}, 'Saint Petersburg': {'Blankets': 100}, 'Kharkiv': {'Food': 150}}
"""