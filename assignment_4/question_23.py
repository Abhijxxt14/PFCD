# Question 23
# Using the list given below
# 1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5
# Display a bar chart showing the response frequencies and their percentages of the total responses.

def display_bar_chart(responses):
    total = len(responses)
    
    print("Response Frequency Bar Chart")
    print("=" * 60)
    
    # Count frequencies
    frequencies = {}
    for rating in range(1, 6):
        frequencies[rating] = responses.count(rating)
    
    # Display bar chart
    for rating in range(1, 6):
        count = frequencies[rating]
        percentage = (count / total) * 100
        bar = '*' * count
        print(f"Rating {rating}: {bar:20s} ({count} responses, {percentage:.1f}%)")
    
    print("=" * 60)
    print(f"Total responses: {total}")

# Data
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

display_bar_chart(responses)
