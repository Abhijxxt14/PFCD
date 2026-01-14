# Question 20
# Twenty students were asked to rate on a scale of 1 to 5 the quality of the food 
# in the student cafeteria, with 1 being "awful" and 5 being "excellent." 
# Place the 20 responses in a list: 1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5
# Determine and display the frequency of each rating. Use the built-in (or user-defined) 
# functions and statistics module functions to display the following response statistics: 
# minimum, maximum, range, mean, median, mode, variance and standard deviation.

from statistics import mean, median, mode, variance, stdev

def analyze_responses(responses):
    # Frequency of each rating
    print("Rating Frequencies:")
    for rating in range(1, 6):
        count = responses.count(rating)
        percentage = (count / len(responses)) * 100
        print(f"Rating {rating}: {count} times ({percentage:.1f}%)")
    
    print("\nStatistics:")
    print(f"Minimum: {min(responses)}")
    print(f"Maximum: {max(responses)}")
    print(f"Range: {max(responses) - min(responses)}")
    print(f"Mean: {mean(responses):.2f}")
    print(f"Median: {median(responses)}")
    print(f"Mode: {mode(responses)}")
    print(f"Variance: {variance(responses):.4f}")
    print(f"Standard Deviation: {stdev(responses):.4f}")

# Data
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

print(f"Responses: {responses}")
print(f"Total responses: {len(responses)}\n")

analyze_responses(responses)
