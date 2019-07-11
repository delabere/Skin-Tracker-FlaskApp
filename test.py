import os
import random

os.chdir(r'/Users/jackrickards/Documents/coding/python/CS50W/skin_tracker_app/static/images/')

#takes only image files from images directory
hands = [file for file in os.listdir() if 'jpg' in file]

print(random.sample(hands, 2)[0])
