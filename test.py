import json
import os
import random

# create dictionary for initial hand_data
# os.chdir(r'/Users/jackrickards/Documents/coding/python/CS50W/skin_tracker_app/static/images/')
# hands = [file for file in os.listdir() if 'jpg' in file]
#
# storage = {}
#
# for index, hand in enumerate(hands, 1):
#     storage[hand] = {'position': index, 'times_sorted': 0}

# store data back into json
# with open(r'/Users/jackrickards/Documents/coding/python/CS50W/skin_tracker_app/storage.json', 'w') as f:
#     json.dump(storage, f)


with open(r'/Users/jackrickards/Documents/coding/python/CS50W/skin_tracker_app/storage.json') as json_file:
    storage = json.load(json_file)

hands_data = [[file, storage[file]['position'], storage[file]['times_sorted']]
            for file in storage]
#
# unsorted = [[file, storage[file]['position'], storage[file]['times_sorted']]
#             for file in storage if storage[file]['times_sorted'] == 0]

# prev_sorted = [[file, storage[file]['position'], storage[file]['times_sorted']]
#                for file in storage if storage[file]['times_sorted'] > 0]
#
# prev_sorted = [['testfile_1.jpg', 21, 1], ['testfile_1.jpg', 22, 3], [
#     'testfile_1.jpg', 23, 2], ['testfile_1.jpg', 24, 2]]

random.shuffle(hands_data)
hands_data = (sorted(hands_data, key = lambda x: int(x[2])))
first, second = hands_data.pop(), hands_data.pop()
return first, second

# if len(unsorted) >= 2:
#     random.shuffle(unsorted)
#     first = unsorted.pop()
#     second = unsorted.pop()
# elif (len(unsorted) == 1) and (len(prev_sorted) >= 1):
#     first = unsorted.pop()
#     prev_sorted = (sorted(prev_sorted, key = lambda x: int(x[2])))
#     second = prev_sorted.pop(0)
# else:
#     prev_sorted = (sorted(prev_sorted, key = lambda x: int(x[2])))
#     first = prev_sorted.pop(0)
#     second = prev_sorted.pop(0)
