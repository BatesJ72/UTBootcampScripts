import os
import csv

path = os.path.join('..', 'Resources', 'netflix_ratings.csv')

search_title = input("Enter a movie title: ")

with open(path, 'r') as file:
    
    dict_reader = csv.DictReader(file)
    
    for row in dict_reader:
        print(row)
        break