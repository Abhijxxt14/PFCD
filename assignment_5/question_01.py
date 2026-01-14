# Question 1
# Write a program to accept student name and marks from the user and create a dictionary. 
# Also, display student marks by taking student name as input.

def manage_student_marks():
    students = {}
    
    while True:
        print("\n--- Student Marks Management ---")
        print("1. Add student")
        print("2. Display student marks")
        print("3. Display all students")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            marks = float(input("Enter marks: "))
            students[name] = marks
            print(f"Student {name} added with marks {marks}")
            
        elif choice == '2':
            name = input("Enter student name to search: ")
            if name in students:
                print(f"{name}'s marks: {students[name]}")
            else:
                print(f"Student {name} not found!")
                
        elif choice == '3':
            if students:
                print("\nAll students:")
                for name, marks in students.items():
                    print(f"{name}: {marks}")
            else:
                print("No students in the database!")
                
        elif choice == '4':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice!")

# Run the program
manage_student_marks()
