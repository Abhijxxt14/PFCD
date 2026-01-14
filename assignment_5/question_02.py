# Question 2
# Write a program to enter names and percentage of marks in a dictionary and 
# display the information on the screen.

def student_info_display():
    students = {}
    
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        print(f"\nStudent {i+1}:")
        name = input("Enter student name: ")
        percentage = float(input("Enter percentage: "))
        students[name] = percentage
    
    print("\n" + "="*50)
    print("Student Information")
    print("="*50)
    print(f"{'Name':<20} {'Percentage'}")
    print("-"*50)
    
    for name, percentage in students.items():
        print(f"{name:<20} {percentage}%")
    
    print("="*50)

# Run the program
student_info_display()
