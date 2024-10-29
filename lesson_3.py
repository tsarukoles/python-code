// Task_1

myStr = input("Enter your text:")
print(myStr[::-1])

// Task_2

import string

letters = 0
number = 0
myStr = input("Enter your text:")
for i in myStr:
    if i in string.ascii_letters:
        letters += 1
    if i in string.digits:
        number += 1
print(myStr)
print("Number of letters:", letters)
print("Number of numbers:", number)

// Task_3

myStr = input("Enter your text:")
myFind = input("Enter your search:")
print("Count results: ", myStr.count(myFind))

// Task_4

myStr = input("Enter your text:")
myFind = input("Enter your search:")
print("Count result: ", myStr.count(myFind))

// Task_5

myStr = input("Enter your text:")
myFind = input("Enter your search:")
mySwap = input("Enter your value to change:")
result = myStr.replace(myFind, mySwap)
print(result)

// Task_6

myStr = input("Enter your text:")
if myStr.lower() == myStr[::-1].lower():
    print("This is a palinndrom:", myStr)

// Task_7

myStr = input("Enter your text:")
myRes = input("Enter reserved words:")
myList = myRes.split()
myStrList = myStr.split()
for word in range(len(myStrList)):
    if myStrList[word] in myList:
        myStrList[word] = myStrList[word].upper()
result = " ".join(myStrList)
print(result)

// Task_8

myStr = ("If thou should live three thousand, or as many as ten thousands of years, yet remember this, that man can "
         "part with no life properly, save with that little part of life, which he now lives: and that which he "
         "lives, is no other, than that which at every instant he parts with. That then which is longest of duration, "
         "and that which is shortest, come both to one effect. For although in regard of that which is already past "
         "there may be some inequality, yet that time which is now present and in being, is equal unto all men. And "
         "that being it which we part with whensoever we die, it doth manifestly appear, that it can be but a moment "
         "of time, that we then part with. For as for that which is either past or to come, a man cannot be said "
         "properly to part with it. For how should a man part with that which he hath not? These two things therefore "
         "thou must remember. First, that all things in the world from all eternity, by a perpetual revolution of the "
         "same times and things ever continued and renewed, are of one kind and nature; so that whether for a hundred "
         "or two hundred years only, or for an infinite space of time, a man see those things which are still the "
         "same, it can be no matter of great moment. And secondly, that that life which any the longest liver, "
         "or the shortest liver parts with, is for length and duration the very same, for that only which is present, "
         "is that, which either of them can lose, as being that only which they have; for that which he hath not, "
         "no man can truly be said to lose.")
myCount = myStr.count(".")
myCount+=myStr.count("!")
myCount+=myStr.count("?")
print(myCount)
count=0
for i in myStr:
    if i == "." or i == "!" or i == "?":
        count+=1
print(count)
print(ord("."))

// Task_9

myStr = input("Enter a string: ")
myStrRev = myStr[::-1]
print(myStrRev)

// Task_10

digits = 0
letters = 0
myStr = input("Enter a string: ")
for i in range(len(myStr)):
    if myStr[i].isdigit():
        digits += 1
    elif myStr[i].isalpha():
        letters += 1
print("Digits: ", digits, "Letters: ", letters)

// Task_11

myStr = input("Enter a string: ")
myCheck = input("Enter the symbol to find: ")
result = myStr.count(myCheck)
print(result)

// Task_12

myStr = input("Enter a string: ")
myFind = input("Enter a search word: ")
print(myStr.count(myFind))

// Task_13

myStr = input("Enter a string: ")
myFind = input("Enter a search word: ")
myChange = input("Enter a change word: ")
myStrList = myStr.split()
for i in range(len(myStrList)):
    if myStrList[i] == myFind:
        myStrList[i] = myChange
result = " ".join(myStrList)
print(result)

// Task_14

digits = 0
symbols = 0
exclamations = 0
myStr = input("Enter a string: ")
choice = input("Enter your choice:\n1. Capital\n2. Digits\n3. Symbols\n4. Exclamations\n0. Exit\n")
myStrList = myStr.split()
while choice != 0:
    if choice == 1:
        print(myStr.title())
    elif choice == 2:
        for i in range(len(myStr)):
            if myStrList[i].isdigit():
                digits += 1
        print("Digits: ", digits)
    elif choice == 3:
        for i in range(len(myStr)):
            if myStrList[i] == "," or myStrList[i] == "." or myStrList[i] == "?" or myStrList[i] == ":" or myStrList[i] == ";":
                symbols += 1
        print("Symbols: ", symbols)
    elif choice == 4:
        for i in range(len(myStr)):
            if myStrList[i] == "!":
                exclamations += 1
        print("Exclamations: ", exclamations)
    choice = input("Enter your choice:\n1. Capital\n2. Digits\n3. Symbols\n4. Exclamations\n0. Exit\n")

// Task_15

myList = []
choice = input("Would you like to add to the list type: yes/no\n")
while choice != "no":
    if choice == "yes":
        myList.append(int(input("Enter a number: ")))
    choice = input("Would you like to add more: yes/no\n")
myFind = int(input("Enter a number to find:"))
result = myList.count(myFind)
print(myList)
print(result)

// Task_16

myList = []
mySum = 0
choice = input("Would you like to add to the list type: yes/no\n")
while choice != "no":
    if choice == "yes":
        myList.append(int(input("Enter a number: ")))
    choice = input("Would you like to add more: yes/no\n")
for i in myList:
    mySum += i
print(mySum)
print(mySum / len(myList))

// Task_17


expression = input("Enter your expression or exit with X: ")
while expression != "X" and expression != "x":
    for operator in ['+', '-', '*', '/']:
        if operator in expression:
            left, right = expression.split(operator)
            left = float(left.strip())
            right = float(right.strip())
            if operator == '+':
                result = left + right
            elif operator == '-':
                result = left - right
            elif operator == '*':
                result = left * right
            elif operator == '/':
                if right != 0:
                    result = left / right
                else:
                    result = "Invalid division"
            print("Result:", result)
    expression = input("Enter your expression or exit with X: ")
print("Exit")
expression=input()
result=eval(expression)
print(result)

// Task_18

import re
pattern=r'(\d+)([\+\-\*/])(\d+)'
match=re.match(pattern,expression)
if match:
    num1=int(match.group(1))
    op=match.group(2)
    num2=int(match.group(3))
    if op=='+':
        res=num1+num2
print(res)

// Task_19

expression=input()
op=['+','-','*','/']
for oper in op:
    if oper in expression:
        parts=expression.split(oper)
        num1=int(parts[0])
        num2=int(parts[1])
        if oper=='+':
            result=num1+num2

print(result)

// Task_20

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

// Task_21

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

// Task_22

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

// Task_23

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
