"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
from visual import NumberOfReviews
from visual import SingleBarChart
import csv
records = []
headings = []
def database(disneydata):
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
    elif choiceA == 'C':
        SubmenuAC()
     

def SubmenuB():
    print("\nPlease enter one of the following options:")
    parkinfoname = Constants.parkinfo
    for item in parkinfoname:
        print(item)
    choiceA = input().upper()
    if choiceA == 'A':
        NumberOfReviews()
    elif choiceA == 'B':
        SingleBarChart()

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
    ParkAndLocationC()
                   
    
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

def ParkAndLocationC():
    with open(disneydata, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        rows = list(csv_reader)
        data = list(csv_reader)
        for line in csv_reader:
            records.append(line)
    RatingIndex = header.index('Rating')
    reviewer_location_index = header.index('Reviewer_Location')
    branch_index = header.index('Branch')
    grouped_data = {}
    for row in rows:
        rating = int(row[RatingIndex])
        ReviewerLocation = row[reviewer_location_index]
        branch = row[branch_index]
        key = (ReviewerLocation, branch)
        grouped_data[key] = grouped_data.get(key, 0) + rating
    grouped_data_list = [(location, branch, total_rating) for (location, branch), total_rating in grouped_data.items()]
    grouped_data_list.sort(key=lambda x: x[2], reverse=True)
    print("Reviewer_Location, Branch, Total_Rating")
    for location, branch, total_rating in grouped_data_list:
        print(f"{location}, {branch}, {total_rating}")     
            
def SubmenuAC():
    with open(disneydata, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        rows = list(csv_reader)
        data = list(csv_reader)
        for line in csv_reader:
            records.append(line)
    RatingIndex = header.index('Rating')
    reviewer_location_index = header.index('Reviewer_Location')
    year_index = header.index('Year_month')
    grouped_data = {}
    for row in rows:
        rating = int(row[RatingIndex])
        ReviewerLocation = row[reviewer_location_index]
        year = row[year_index]
        key = (ReviewerLocation, year)
        grouped_data[key] = grouped_data.get(key, 0) + rating
    grouped_data_list = [(location, year, total_rating) for (location, year), total_rating in grouped_data.items()]
    grouped_data_list.sort(key=lambda x: x[2], reverse=True)
    print("Reviewer_Location, year, Total_Rating")
    for location, year, total_rating in grouped_data_list:
        print(f"{location}, {year}, {total_rating}") 
            
            
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
   