"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import json
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

def ReviewByMonthHongKong():
 

    monthly_ratings = {}

    
    with open('data/disneyland_reviews.csv', 'r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)

      for row in reader:
        if row['Branch'] == 'Disneyland_HongKong':
          year_month_parts = row['Year_Month'].split('-')
          if len(year_month_parts) == 2:
            month = int(year_month_parts[1])
            monthly_ratings.setdefault(month, {'sum': 0, 'count': 0})
            monthly_ratings[month]['sum'] += int(row['Rating'])
            monthly_ratings[month]['count'] += 1
    average_ratings = {}
    for month, data in monthly_ratings.items():
      average_ratings[month] = data['sum'] / data['count']
    month_names = []
    avg_ratings = []

    for month in sorted(average_ratings.keys()):
      month_names.append(month)
      avg_ratings.append(average_ratings[month])

    plt.figure(figsize=(10, 6))
    plt.bar(month_names, avg_ratings, color='skyblue')
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Average Rating', fontsize=12)
    plt.title('Average Rating for Disneyland Hong Kong by Month', fontsize=14)
    plt.xticks(month_names, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=10)
    plt.grid(axis='y', linestyle='--')
    plt.show()

def ReviewByMonthParis():
 

    monthly_ratings = {}

    
    with open('data/disneyland_reviews.csv', 'r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)

      for row in reader:
        if row['Branch'] == 'Disneyland_Paris':
          year_month_parts = row['Year_Month'].split('-')
          if len(year_month_parts) == 2:
            month = int(year_month_parts[1])
            monthly_ratings.setdefault(month, {'sum': 0, 'count': 0})
            monthly_ratings[month]['sum'] += int(row['Rating'])
            monthly_ratings[month]['count'] += 1
    average_ratings = {}
    for month, data in monthly_ratings.items():
      average_ratings[month] = data['sum'] / data['count']
    month_names = []
    avg_ratings = []

    for month in sorted(average_ratings.keys()):
      month_names.append(month)
      avg_ratings.append(average_ratings[month])

    plt.figure(figsize=(10, 6))
    plt.bar(month_names, avg_ratings, color='skyblue')
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Average Rating', fontsize=12)
    plt.title('Average Rating for Disneyland Paris by Month', fontsize=14)
    plt.xticks(month_names, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=10)
    plt.grid(axis='y', linestyle='--')
    plt.show()


def ReviewByMonthCalifornia():
 

    monthly_ratings = {}

    
    with open('data/disneyland_reviews.csv', 'r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)

      for row in reader:
        if row['Branch'] == 'Disneyland_California':
          year_month_parts = row['Year_Month'].split('-')
          if len(year_month_parts) == 2:
            month = int(year_month_parts[1])
            monthly_ratings.setdefault(month, {'sum': 0, 'count': 0})
            monthly_ratings[month]['sum'] += int(row['Rating'])
            monthly_ratings[month]['count'] += 1
    average_ratings = {}
    for month, data in monthly_ratings.items():
      average_ratings[month] = data['sum'] / data['count']
    month_names = []
    avg_ratings = []

    for month in sorted(average_ratings.keys()):
      month_names.append(month)
      avg_ratings.append(average_ratings[month])

    plt.figure(figsize=(10, 6))
    plt.bar(month_names, avg_ratings, color='skyblue')
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Average Rating', fontsize=12)
    plt.title('Average Rating for Disneyland California by Month', fontsize=14)
    plt.xticks(month_names, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=10)
    plt.grid(axis='y', linestyle='--')
    plt.show()
    
    

def MenuAD():
 

 park_location_ratings = {}
 
 with open('data/disneyland_reviews.csv', 'r', newline='', encoding='utf-8') as file:
     reader = csv.DictReader(file)
 
     for row in reader:
         park_name = row['Branch']
         reviewer_location = row['Reviewer_Location']
         rating = int(row['Rating'])
 
         if park_name not in park_location_ratings:
             park_location_ratings[park_name] = {}
 
         if reviewer_location not in park_location_ratings[park_name]:
             park_location_ratings[park_name][reviewer_location] = {'sum': 0, 'count': 0}
 
         park_location_ratings[park_name][reviewer_location]['sum'] += rating
         park_location_ratings[park_name][reviewer_location]['count'] += 1
 
 average_park_location_ratings = {}
 
 for park_name, location_data in park_location_ratings.items():
     average_park_location_ratings[park_name] = {}
     for location, data in location_data.items():
         average_park_location_ratings[park_name][location] = data['sum'] / data['count']
 
 for park_name, location_ratings in average_park_location_ratings.items():
     print(f"\nAverage ratings for {park_name}:")
     for location, avg_rating in location_ratings.items():
         print(f"  {location}: {avg_rating:.2f}")
         


##### export menu #####

class DataExporter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.aggregates = {}

    def calculate_aggregates(self):
        with open(self.file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                park = row['Branch']
                rating = int(row['Rating'])
                country = row['Reviewer_Location']

                if park not in self.aggregates:
                    self.aggregates[park] = {
                        'num_reviews': 0,
                        'num_positive': 0,
                        'total_score': 0,
                        'countries': set()
                    }

                self.aggregates[park]['num_reviews'] += 1
                self.aggregates[park]['total_score'] += rating
                self.aggregates[park]['countries'].add(country)
                if rating >= 4:  # Assuming 4 and 5 are positive
                    self.aggregates[park]['num_positive'] += 1

        # Calculate average scores
        for park in self.aggregates:
            self.aggregates[park]['avg_score'] = self.aggregates[park]['total_score'] / self.aggregates[park]['num_reviews']
            self.aggregates[park]['num_countries'] = len(self.aggregates[park]['countries'])

    def export_to_txt(self, output_file):
        with open(output_file, 'w') as file:
            for park, data in self.aggregates.items():
                file.write(f"Park: {park}\n")
                for key, value in data.items():
                    file.write(f"  {key}: {value}\n")

    def export_to_csv(self, output_file):
        with open(output_file, 'w', newline='') as file:
            fieldnames = ['Park', 'num_reviews', 'num_positive', 'avg_score', 'num_countries']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for park, data in self.aggregates.items():
                data['Park'] = park
                writer.writerow(data)

    def export_to_json(self, output_file):
        with open(output_file, 'w') as file:
            json.dump(self.aggregates, file, indent=4)

def main_menu():
    while True:
        print("\nDisneyland Reviews Analysis")
        print("A. Export Data")
        print("D. Exit")

        choice = input("Enter your choice: ").upper()

        if choice == 'A':
            print("\nChoose export format:")
            print("1. TXT")
            print("2. CSV")
            print("3. JSON")
            format_choice = input("Enter your choice: ")

            exporter = DataExporter('data/disneyland_reviews.csv')
            exporter.calculate_aggregates()

            if format_choice == '1':
                exporter.export_to_txt('data/disneyland_aggregates.txt')
                print("Data exported to disneyland_aggregates.txt")
            elif format_choice == '2':
                exporter.export_to_csv('data/disneyland_aggregates.csv')
                print("Data exported to disneyland_aggregates.csv")
            elif format_choice == '3':
                exporter.export_to_json('data/disneyland_aggregates.json')
                print("Data exported to disneyland_aggregates.json")
            else:
                print("Invalid format choice.")
        elif choice == 'D':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
