# Task_410

numberOne = int(input("Enter the first number of the range: "))
numberTwo = int(input("Enter the second number of the range: "))
number = int(input("Enter the number: "))
while number>numberTwo or number<numberOne:
    number = int(input("Enter the number: "))
for i in range(numberOne,numberTwo+1):
    if i == number:
        print("!",i,"!",end=" ",sep="")
    else:
        print(i,end=" ")