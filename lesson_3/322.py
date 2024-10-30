# Task_322

import random

list1 = []
evenNumbers = []
oddNumbers = []
negativeNumbers = []
positiveNumbers = []

for i in range(20):
    list1.append(random.randint(-20,20))
print(list1)

for i in range(len(list1)):
    if list1[i] % 2 == 0:
        evenNumbers.append(list1[i])
    if list1[i] % 2 != 0:
        oddNumbers.append(list1[i])
    if list1[i] < 0:
        negativeNumbers.append(list1[i])
    if list1[i] > 0:
        positiveNumbers.append(list1[i])
print(evenNumbers)
print(oddNumbers)
print(negativeNumbers)
print(positiveNumbers)