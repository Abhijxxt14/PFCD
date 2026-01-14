# Question 6
# Input 10 integers from the keyboard into a list. The number to be searched is entered 
# through the keyboard by the user. Write a Python program to find if the number to be 
# searched is present in the list and if it is present, display the number of times it appears in the list.

def search_in_list():
    numbers = []
    
    print("Enter 10 integers:")
    for i in range(10):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    print(f"\nList: {numbers}")
    
    search_num = int(input("\nEnter the number to search: "))
    
    if search_num in numbers:
        count = numbers.count(search_num)
        print(f"Number {search_num} is present in the list.")
        print(f"It appears {count} time(s) in the list.")
    else:
        print(f"Number {search_num} is not present in the list.")

# Run the program
search_in_list()
