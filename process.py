"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import csv
def database(disneydata):
    data = []
    with open(disneydata, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
    print("Finished reading the dataset.")
    print(f"The dataset contains {len(data)} rows.")
    print()
    return data

disneydata = 'data/disneyland_reviews.csv'
dataset = database(disneydata)

def SubmenuA():
    print("\nPlease enter one of the following options:")
    firstmenuname = Constants.firstmenu
    for item in firstmenuname:
        print(item)
    choiceA = input().upper()

    if choiceA == 'A':
     print("Which park would you like to see the reviews?")
     SubmenuAA()
    elif choiceA == 'B':
        SubmenuAB()
     

def SubmenuB():
    print("\nPlease enter one of the following options:")
    parkinfoname = Constants.parkinfo
    for item in parkinfoname:
        print(item)
    choiceB = input().upper()

def SubmenuAA():
    print("   [A] California")
    print("   [B] Paris")
    print("   [C] Hong Kong")
    choiceAA = input().upper()

    if choiceAA == 'A':
        ReviewCalifornia()
    elif choiceAA == 'B':
        ReviewParis()
    elif choiceAA == 'C':
        ReviewHongKong()

def SubmenuAB():
    menuparkname = Constants.menupark
    for item in menuparkname:
        print(item)
        
    choice = input("\nPlease enter one of the following options: ").strip().upper()
    if choice == 'A':
        ParkAndLocationC()
    elif choice == 'B':
        print()
        
            
            
    
def ReviewCalifornia():
    for row in dataset:
        if 'Disneyland_California' in row[4]:
            print(row)

def ReviewParis():
    for row in dataset:
        if 'Disneyland_Paris' in row[4]:
            print(row)

def ReviewHongKong():
    for row in dataset:
        if 'Disneyland_HongKong' in row[4]:
            print(row)

    #=def ParkAndLocationC():
    #for row in dataset:
      #  if 'Disneyland_California' in row[4]:
       #     print(row[3,4])
            
            
            
class Constants:
    menupark = [
        "   [A] California",
        "   [B] Paris",
        "   [C] Hong Kong",
    ]
    
    parkinfo = [
        "   [A] Most Reviewed Parks",
        "   [B] Average Scores",
        "   [C] Park Ranking by Nationality",
        "   [D] Most popular Month by Park",
    ]
    firstmenu = [
        "   [A] View Reviews by Park",
        "   [B] Number of Reviews by park and Reviewer Location",
        "   [C] Average Score per year by Park",
        "   [D] Average Score per Park by Reviewer Location",
   ] 
   