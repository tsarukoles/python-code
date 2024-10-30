# Task_320

import random

list1 = []
negative = 0
positive = 0

for i in range(20):
    list1.append(random.randint(-100, 100))
    if list1[i] < 0:
        negative += 1
    elif list1[i] > 0:
        positive += 1
print(list1)
maxValue = list1[0]
minValue = list1[0]  # That was tricky. min and max needed to be below first loop

for i in list1:
    if i >maxValue:
        maxValue = i
    if i< minValue:
        minValue = i

print('Negative count: ', negative)
print('Positive count: ', positive)
print('Max value: ', maxValue)
print('Min value: ', minValue)