import os
import string
import shutil

from film_titles import films_titles
from film_awards import films_awards

film_awards_list = []

for films in films_awards:
  for film_award in films['results']:
    award_info = {
        'award_name': film_award['award_name'],
        'award': film_award['award'],
        'type': film_award['type'],
        'title': film_award['movie']['title']
    }
    film_awards_list.append(award_info)

sorted_film_awards = sorted(film_awards_list, key=lambda x: x['award_name'])

os.mkdir("Harry Potter") # Директорія Гаррі Поттер
for film in films_titles["results"]:
    film_title = film["title"].replace(":", "")
    film_dir = os.path.join("Harry Potter", film_title)
    os.mkdir(film_dir)
    print(f"Створено дерикторію '{film_title}'") # Папки з назв фільмів

# Створення тек для кожної літери в кожній директорії фільму
for film in films_titles["results"]:
    film_title = film["title"].replace(":", "")
    film_dir = os.path.join("Harry Potter", film_title)

    for letter in string.ascii_uppercase:
        letter_dir = os.path.join(film_dir, letter)
        os.mkdir(letter_dir)

print(os.getcwd())
# Розміщення TXT-файлів з нагородами в папки з літерами
for award_info in sorted_film_awards:
  award_name = award_info['award_name']
  award_letter = award_name[0].upper()
  
  for film in films_titles["results"]:
    if award_info['title']==film['title']:
      film_title = film["title"].replace(":", "")
      film_dir = os.path.join("Harry Potter", film_title, award_letter)
# Знайдіть відповідну теку для нагороди
      if os.path.exists(film_dir):
    # Створіть та запишіть інформацію про нагороду в TXT-файл
        file_path = os.path.join(film_dir, f"{award_name}.txt")
        with open(file_path, 'w') as award_file:
          award_file.write(f"Award Name: {award_info['award_name']}\n")
          award_file.write(f"Award Type: {award_info['type']}\n")
          award_file.write(f"Award: {award_info['award']}\n")