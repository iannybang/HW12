#Create directory to store files with film information
import os

os.chdir('video_manager')
new_dir = 'film_player/film_storage'
os.makedirs (new_dir )
os.chdir (new_dir)

import string

for letter in string.ascii_uppercase:
      os.mkdir(letter)

