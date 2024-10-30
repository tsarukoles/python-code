# Task_321

import random

list1 = []
negativeSum = 0
evenSum = 0
oddSum = 0
indexThree = 1

multMinMax = 1
sumMinMax = 0

for i in range(20):
    list1.append(random.randint(-20, 20))
minVal = list1[0]
maxVal = list1[0]
minValueIndex = list1[0]
maxValueIndex = list1[0]
print(list1)
for i in list1:
    if i < 0:
        negativeSum += i
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
    if i % 3 == 0:
        indexThree *= i
for i in range(len(list1)):
    if minVal > list1[i]:
        minValueIndex = i
    if list1[i] > maxVal:
        maxValueIndex = i
if minValueIndex < maxValueIndex:
    for i in list1[minValueIndex:maxValueIndex + 1]:
        sumMinMax += i
        multMinMax *= i
else:
    for i in list1[maxValueIndex:minValueIndex + 1]:
        sumMinMax += i
        multMinMax *= i
print(negativeSum)
print(evenSum)
print(oddSum)
print(indexThree)
print(sumMinMax)
print(multMinMax)