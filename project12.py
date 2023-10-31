import os
os.chdir("./HW12/")

#Крок 1
os.mkdir("Harry Potter")
os.chdir("Harry Potter")

from film_titles import films_titles
for result in films_titles['results']:
  os.mkdir(result['title'])

#Крок 2
import string

for directory in os.listdir():
    os.chdir(directory)
    for a in string.ascii_lowercase:
      os.mkdir(a)
    os.chdir("..")

#Крок3

from film_awards import films_awards

film_lists = []
for film in films_awards:
  film_name = film['results'][0]['movie']['title']
  award_list = []
  for award in film['results']:
    award_list.append({"type":award['type'],"award_name":award['award_name'],"award":award['award']})
  film_lists.append({film_name:award_list})

#Крок4

film_lists_sorted = []
for film_data in film_lists:
  for film_name, awards in film_data.items():
    sorted_awards = sorted(awards, key=lambda x: x['award_name'])
    film_lists_sorted.append({film_name: sorted_awards})

#Крок5

for film_data in film_lists_sorted:
  for film_name, awards in film_data.items():
    for award in awards:
      for folder in os.listdir():
        if film_name == folder:
          os.chdir(folder)
          os.chdir(award["award_name"][0].lower())
          file_path = f"{award['award_name']}.txt"
          with open(file_path, 'w') as file:
            award_name = award['award']
            file.write(award_name)
          os.chdir("..")
          os.chdir("..")


