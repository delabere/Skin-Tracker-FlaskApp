import json
import os


os.chdir(r'/Users/jackrickards/Documents/coding/python/CS50W/skin_tracker_app/static/images/')
hands = [file for file in os.listdir() if 'jpg' in file]

storage = {}

for index, hand in enumerate(hands, 1):
    storage[hand] = {'position': index, 'times_sorted': 0}

with open(r'/Users/jackrickards/Documents/coding/python/CS50W/skin_tracker_app/storage.json', 'w') as f:
    json.dump(storage, f)


with open(r'/Users/jackrickards/Documents/coding/python/CS50W/skin_tracker_app/storage.json') as json_file:
    storage = json.load(json_file)

print(storage)
