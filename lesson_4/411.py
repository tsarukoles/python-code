# Task_411

import random
number=random.randint(1,500)
print(number)

count=0
userAnswer=int(input("Enter you`r number:"))
while userAnswer != number or userAnswer !=0:
    if userAnswer < number:
        print("My number is bigger")
        count+=1
    elif userAnswer>number:
        print("My number is less")
        count+=1
    else:
        print("you win!!")
        break
    if userAnswer == 0:
        break
    userAnswer=int(input("Enter you`re number or zero for exit"))

print("You need ",count,"count")