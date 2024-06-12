"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import csv
import matplotlib.pyplot as plt
with open('data/disneyland_reviews.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) 
        rows = list(csv_reader)

def NumberOfReviews():
   
    park_counts = {}
    for row in rows:
        park_name = row[4]  
        park_counts[park_name] = park_counts.get(park_name, 0) + 1


    parks = list(park_counts.keys())
    counts = list(park_counts.values())


    plt.figure(figsize=(10, 8))
    plt.pie(counts, labels=parks, autopct='%1.1f%%', startangle=140)
    plt.title('Number of Reviews per Park')
    plt.axis('equal')


    plt.show()

def SingleBarChart():
    park_ratings = {}
    for row in rows:
        park_name = row[4]  
        rating = int(row[1])  
        if park_name not in park_ratings:
            park_ratings[park_name] = []
        park_ratings[park_name].append(rating)


    average_ratings = {}
    for park_name, ratings in park_ratings.items():
        average_ratings[park_name] = sum(ratings) / len(ratings)


    parks = list(average_ratings.keys())
    avg_ratings = list(average_ratings.values())


    plt.figure(figsize=(10, 6))
    plt.bar(parks, avg_ratings, color='skyblue')
    plt.xlabel('Park')
    plt.ylabel('Average Rating')
    plt.title('Average Rating per Park')
    plt.xticks(rotation=45, ha='right')  


    plt.show()
