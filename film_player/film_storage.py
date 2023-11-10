#Create directory to store files with film information
import os
import string

new_dir = 'film_player/film_storage'
os.makedirs (new_dir )
os.chdir (new_dir)

for letter in string.ascii_uppercase:
      os.mkdir(letter)
