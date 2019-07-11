import random as rnd

items = {}

items[1] = [6,0]
items[2] = [5,0]
items[3] = [4,0]
items[4] = [3,0]
items[5] = [2,0]
items[6] = [1,0]

new_items = {}


#sorting for new items
def newSorter(key):
    items[key] = [0,0]
    octile = list(items)[int(len(items)*0.125)]-1
    if octile == 0:
        octile += 1
    answer = input(f'Is {key} larger than {octile * 4}?\n(y or n)> ')
    if answer == 'y':
        answer = input(f'Is {key} larger than {octile * 6}?\n(y or n)> ')
        if answer == 'y':
            Shifter(items, octile * 7)
            items[key] = [octile * 7,0]
        if answer == 'n':
            Shifter(items, octile * 5)
            items[key] = [octile * 5,0]
    elif answer == 'n':
        answer = input(f'Is {key} larger than {list(items)[int(len(items)*0.25)]}?\n(y or n)> ')
        if answer == 'y':
            Shifter(items, octile * 3)
            items[key] = [octile * 3,0]
        if answer == 'n':
            Shifter(items, octile * 1)
            items[key] = [octile * 1,0]

def Shifter(dic, pos):
    count = 1
    for key, value in dic.items():
        if pos <= count:
            dic[key][0] = dic[key][0]+1
        count += 1


#function takes two integers and assigns them a position value based on user input
def swapSorter(num1, num2):
    if items[num1] == items[num2]:
        print('same numbers passed to sorter')
        pass
    else:
        answer = input(f'Is {num1} bigger than {num2}?\n(y or n)> ')
        if answer == 'y':
            if items[num1] > items[num2]:
                items[num1][1] = items[num1][1] + 1
                items[num2][1] = items[num2][1] + 1
                pass
            else:
                a = items[num1][0]
                items[num1][1] = items[num1][1] + 1
                items[num2][1] = items[num2][1] + 1
                items[num1][0] = items[num2][0]
                items[num2][0] = a
        elif answer == 'n':
            if items[num1] < items[num2]:
                items[num1][1] = items[num1][1] + 1
                items[num2][1] = items[num2][1] + 1
                pass
            else:
                a = items[num1][0]
                items[num1][1] = items[num1][1] + 1
                items[num2][1] = items[num2][1] + 1
                items[num1][0] = items[num2][0]
                items[num2][0] = a


#random selection sorting
while True:
    swapSorter(rnd.randint(1,(len(items))),rnd.randint(1,(len(items))))

#sorting with preference given to least sorted
while True:
    sort_list = []
    for i in list(items.values()):
        sort_list.append(i[1])
    least = min(sort_list)
    for key, value in list(items.items()):
        if value[1] == least:
            x = key
    swapSorter(x, rnd.randint(1,(len(items))))


#creating new item
def createItem():
    new_items[len(items)+len(new_items)+1] = 'unrated'


#sorting for new entries
while 'unrated' in list(new_items.values()):
    for key in list(new_items.keys()):
            newSorter(key)
            new_items.pop(key)
