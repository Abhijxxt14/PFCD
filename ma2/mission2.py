"""
Mission 2: High Alert Identification
Task: To identify cities requiring aid using set operations
"""

def high_alert_identification(cleaned_cities, previous_intel):
    cleaned_set = set(cleaned_cities)
    intel_set = set(previous_intel)
    
    all_cities = cleaned_set | intel_set
    unique_cities = cleaned_set ^ intel_set
    high_alert_cities = cleaned_set & intel_set
    
    return sorted(all_cities), sorted(unique_cities), sorted(high_alert_cities)

cleaned_cities = ["Dnipro", "Kharkiv", "Kyiv", "Lviv", "Odessa"]
previous_intel = ["Kyiv", "Mariupol", "Lviv", "Donetsk"]
    
all_cities, unique_cities, high_alert = high_alert_identification(cleaned_cities, previous_intel)
    
print("Cleaned cities:", cleaned_cities)
print("Previous intel:", previous_intel)
print("\nOutput:")
print("All cities requiring aid:", all_cities)
print("Unique cities:", unique_cities)
print("High alert cities:", high_alert)


"""
Expected Output:

Cleaned cities: ['Dnipro', 'Kharkiv', 'Kyiv', 'Lviv', 'Odessa']
Previous intel: ['Kyiv', 'Mariupol', 'Lviv', 'Donetsk']
Output:
All cities requiring aid: ['Dnipro', 'Donetsk', 'Kharkiv', 'Kyiv', 'Lviv', 'Mariupol', 'Odessa']
Unique cities: ['Dnipro', 'Donetsk', 'Kharkiv', 'Mariupol', 'Odessa']
High alert cities: ['Kyiv', 'Lviv']
"""