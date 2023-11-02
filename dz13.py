import json
import os
import csv

from genres import ganres

#Крок1
genre_list = json.loads(ganres)

#Крок2
os.mkdir('Genres')
os.chdir('Genres')

for genre in genre_list['results']:
    os.mkdir(genre['genre'])


#Крок3
csv_columns =['title','year','rating','type','genres']
csv_file_name = "film_info.csv"

for folder in os.listdir():
  csv_file_path = os.path.join(folder, csv_file_name)
  with open(csv_file_path, 'w',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_columns)

#Крок4

from films_data import films_data

for folder in os.listdir():
    for film in films_data:
        for genre_data in film['gen']:
            if genre_data['genre'] == folder:
                csv_file_path = os.path.join(folder, csv_file_name)
                with open(csv_file_path,'a') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([film['title'],film['year'],film['rating'],film['type'], ';'.join(genre_data['genre'] for genre_data in film['gen'])])

