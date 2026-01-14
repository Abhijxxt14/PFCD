# Question 3
# Design and develop a menu-driven Python program for the following list operations.
# a. Create a list of N integers
# b. Display the list elements
# c. Insert an element at a specific position
# d. Delete an element at a given position
# e. Exit

def menu_driven_list():
    my_list = []
    
    while True:
        print("\n--- List Operations Menu ---")
        print("a. Create a list of N integers")
        print("b. Display the list elements")
        print("c. Insert an element at a specific position")
        print("d. Delete an element at a given position")
        print("e. Exit")
        
        choice = input("Enter your choice (a/b/c/d/e): ").lower()
        
        if choice == 'a':
            n = int(input("Enter the size of the list: "))
            my_list = []
            for i in range(n):
                element = int(input(f"Enter element {i+1}: "))
                my_list.append(element)
            print(f"List created: {my_list}")
            
        elif choice == 'b':
            if my_list:
                print(f"List elements: {my_list}")
            else:
                print("List is empty!")
                
        elif choice == 'c':
            if my_list:
                element = int(input("Enter the element to insert: "))
                position = int(input("Enter the position (0-based index): "))
                if 0 <= position <= len(my_list):
                    my_list.insert(position, element)
                    print(f"Element inserted. Updated list: {my_list}")
                else:
                    print("Invalid position!")
            else:
                print("List is empty! Create a list first.")
                
        elif choice == 'd':
            if my_list:
                position = int(input("Enter the position to delete (0-based index): "))
                if 0 <= position < len(my_list):
                    deleted = my_list.pop(position)
                    print(f"Element {deleted} deleted. Updated list: {my_list}")
                else:
                    print("Invalid position!")
            else:
                print("List is empty!")
                
        elif choice == 'e':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice! Please try again.")

# Run the program
menu_driven_list()
