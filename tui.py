"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilize any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

#from process import disneydata
from process import SubmenuA
from process import SubmenuB



def menu():
    print("Please enter the letter which corresponds with your desired menu choice:")
    print("   [A] View Data")
    print("   [B] Visualise Data")
    print("   [X] Exit")
    choice = input().upper()
    
   
    if choice == 'A':
        print("You Have chosen option A - View Data")
        SubmenuA()  # Call function to view data
    elif choice == 'B':
        print("You have chosen option B - Visualize Data")
        SubmenuB()
        #visualize_data()  # Call function to visualize data
    elif choice == 'X':
        print("Exiting program...")
        #break  # Exit the loop
    else:
        input("Invalid choice. Please try again.").upper()

# Placeholder functions (replace with your actual data handling)
#def view_data():
#   print("This is where you would implement viewing the data.")

#def visualize_data():
#   print("This is where you would implement data visualization.")

menu()
