"""
Mission 3: Detailed City Intel
Task: To create dictionary with city information and calculate totals
"""

def detailed_city_intel(high_alert_cities, city_data):
    high_alert_cities_info = {}
    
    for city, population, aid_requests in city_data:
        if city in high_alert_cities:
            high_alert_cities_info[city] = (city, population, aid_requests)
    
    total_population = sum(data[1] for data in high_alert_cities_info.values())
    total_aid_requests = sum(data[2] for data in high_alert_cities_info.values())
    
    return high_alert_cities_info, total_population, total_aid_requests

high_alert_cities = ["Kyiv", "Lviv"]
city_data = [
    ("Kyiv", 2800000, 250),
    ("Kharkiv", 1431000, 180),
    ("Lviv", 721301, 90),
    ("Odessa", 1029049, 120)
]
    
cities_info, total_pop, total_aid = detailed_city_intel(high_alert_cities, city_data)
    
print("High alert cities:", high_alert_cities)
print("City data:", city_data)
print("\nOutput:")
print("High alert cities info:", cities_info)
print("Total population:", total_pop)
print("Total aid requests:", total_aid)



"""
Expected Output:

High alert cities: ['Kyiv', 'Lviv']
City data: [('Kyiv', 2800000, 250), ('Kharkiv', 1431000, 180), ('Lviv', 721301, 90), ('Odessa', 1029049, 120)]
Output:
High alert cities info: {'Kyiv': ('Kyiv', 2800000, 250), 'Lviv': ('Lviv', 721301, 90)}
Total population: 3521301
Total aid requests: 340
"""