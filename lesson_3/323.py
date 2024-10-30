# Task_323

import random

listOne = []
listTwo = []
listThree = []
noRepeat = []
sameElements = []
uniqueElements = []
minOne = 0
maxOne = 0
minTwo = 0
maxTwo = 0

for i in range(10):
    listOne.append(random.randint(-10, 10))
    listTwo.append(random.randint(-10, 10))

listThree = listOne[:] + listTwo[:]  # Elements of both arrays

for element in listOne:  # Elements with noRepeat
    if element not in noRepeat:
        noRepeat.append(element)
for element in listTwo:
    if element not in noRepeat:
        noRepeat.append(element)
print("check")
for i in listOne:  # Same Elements in both lists
    if i in listTwo and i not in sameElements:
        sameElements.append(i)

for i in listOne:  # Unique elements for both lists
    if i not in listTwo and i not in uniqueElements:
        uniqueElements.append(i)
for i in listTwo:
    if i not in listOne and i not in uniqueElements:
        uniqueElements.append(i)

for num in listOne:  # MinMax list 1
    if num < minOne:
        minOne = num
    if num > maxOne:
        maxOne = num
for num in listTwo:  # MinMax list 2
    if num < minTwo:
        minTwo = num
    if num > maxTwo:
        maxTwo = num

print("List 1: ", listOne)
print("List 2: ", listTwo)
print("List 1 and List 2: ", listThree)
print("Elements that doesn't repeat: ", noRepeat)
print("Check")
print("Same elements in List 1 and List 2: ", sameElements)
print("Unique elements of List 1 and List 2: ", uniqueElements)
print("Min value List 1: ", minOne, " Max value List 1: ", maxOne)
print("Min value List 2: ", minTwo, " Max value List 2: ", maxTwo)