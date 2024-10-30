# Task_401

number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))
while number_one < number_two:
    print(number_one)
    number_one +=1

# Task_402

number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))
while number_one < number_two:
    number_one += 1
    if number_one % 2 == 0:
        continue
    print(number_one)

# Task_403

number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))
while number_one < number_two:
    number_one += 1
    if number_one % 2 == 1:
        continue
    print(number_one)

# Task_404

number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))
while number_two > number_one:
    number_two -= 1
    print(number_two)

# Task_405

number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))
for number_one in range(number_one - 1, number_two):
    number_one += 1
    if number_one % 2 == 0:
        continue
    print(number_one)

# Task_406

odd_five = 0
number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))
print("Range numbers:")
for i in range(number_one, number_two + 1):
    print(i)
    if i % 7 == 0:
        print("odd seven",i)
    if i%5==0:
        odd_five+=1
print("Range numbers in descending order:")
for number in range(number_two, number_one - 1, - 1):
    print(number)
print("count odd 5",odd_five)

# Task_407

number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))
for number in range(number_one, number_two + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Task_408

number = int(input("Enter the number to multiply:"))
for i in range(1, 10):
    print(number, "*", i, "=", number * i)

# Task_409

useChoice=int(input("Enter what kind of currency you wnat to chage\n1-dollars to grn\n2-grn to dollars\n0- for exit"))

while useChoice!=0:
    amount = float(input("Enter how much money you will change: "))
    if useChoice==1:
        print("you will have",amount*41.5,"grn")
    elif useChoice==2:
        print("you will have",amount/41.5,"$")
    useChoice = int(
        input("Enter what kind of currency you wnat to chage\n1-dollars to grn\n2-grn to dollars\n0- for exit"))

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

# Task_412

x = int(input("Enter numer X: "))
y = int(input("Enter number Y: "))
pow = x
for i in range(y):
    pow *= x
print(pow)

for i in range(1,10):
    for j in range(1,10):
        print(i*j,end="\t")
    print()

# Task_412a

floor = 1
energy = 80
print("i'm on the", floor, "floor")
while floor != 5:
    step = 0
    while step != 20:
        step += 1
        energy -= 1
        if energy == 0:
            print("I'm tired")
            energy += 70
    floor += 1
    print("I'm on the", floor, "floor")
print("I'm done")

# Task_413

amount = 0
for i in range(100, 1000):
    number = i
    numberThree = number % 10  #10 0
    number //= 10  #10
    numberTwo = number % 10  #1 0
    number //= 10  #1
    if numberThree == numberTwo or numberThree == number or numberTwo == number:
        amount += 1
print(amount)

# Task_414

amount = 0
for i in range(100, 10000):
    number = i
    numberFour = number % 10  #100 0
    number //= 10  #1000
    numberThree = number % 10  #10 0
    number //= 10  #100
    numberTwo = number % 10  #1 0
    number //= 10  #1
    if numberFour != numberThree and numberFour != numberTwo and numberFour != number and numberThree != numberTwo and numberThree != number and numberTwo != number:
        amount = amount + 1
print(amount)

# Task_415

result = 0
decimal = 1
number = int(input("Enter a number: "))
while number != 0:
    if number%10!=3 and number%10!=6:
        result+=number%10*decimal
        decimal*=10
    number//=10
print(result)
number = input()
result = ""
for i in number:
    if i != "3" and i != "6":
        result += i

print(result)

# Task_416

number = int(input("Enter a number: "))
for i in range(number):
    for j in range(number):
        print("*", end="\t")
    print()

# Task_417

width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
for i in range(height):
    for j in range(width):
        print("*", end="\t")
    print()

# Task_417a

number = int(input("Enter a number: "))
for i in range(number):
    for j in range(number):
        if i == 0 or i == number-1 or j == 0 or j == number-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

# Task_418

width = int(input("Enter the width:"))
height = int(input("Enter the height:"))
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Task_419

start = int(input("Enter a start number: : "))
end = int(input("Enter an end number: "))

print("Numbers", start, "to", end, ":")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')

# Task_420

numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
for i in range(numberOne, numberTwo + 1):
    for j in range(1, 10 + 1):
        print(i, "*", j, "=", i * j, end="\t")
    print()

# Task_421

total = 0
count = 0
zero = 0
number = int(input("Enter a number: "))
while number > 0:
    digit = number % 10
    number //= 10
    count += 1
    total += digit
    if digit == 0:
        zero += 1
userChoice = int(input("Your choice:\n1. Amount of digits\n2. Sum of you digits\n3. Average of your digits\n4. Amount of 0's\n0. Exit\n"))
while userChoice != 0:
    if userChoice == 1:
        print("Your number of digits is: ", count)
    elif userChoice == 2:
        print("Your sum of digits is: ", total)
    elif userChoice == 3:
        print("Your average of digits is: ", total/count)
    elif userChoice == 4:
        print("Your number of 0s is: ", zero)
    else:
        print("Invalid choice")
    userChoice = int(input("Your choice:\n1. Amount of digits\n2. Sum of you digits\n3. Average of your digits\n4. Amount of 0's\n0. Exit\n"))
print("Thank you!")

# Task_422

#***---***---***---***---
#***---***---***---***---
#***---***---***---***---
#---***---***---***---***
#---***---***---***---***
#---***---***---***---***

rows = 8
cols = 8
size = int(input("Enter the size of the cell: "))
for i in range(size):
    for j in range(size):
        if i == 0 and j == 4 or i == 1 and 3 <= j <= 5 or i == 2 and 2 <= j <= 6 or i == 3 and 1 <= j <= 7 or i == 4 and 0 <= j <= 9 or i == 5 and 1 <= j <= 7 or i == 6 and 2 <= j <= 6 or i == 7 and 3 <= j <= 5 or i == 8 and j == 4:
            print("*",end="")
        else:
            print(" ", end="")
    print()

# Task_423

n=5
for i in range(2*n-1):
    if i<n:
        spaces=n-i-1
        stars=2*i+1
    else:
        spaces=i-n+1
        stars=2*(2*n-i-1)-1
    print(' '*spaces+'*'*stars)

# Task_424

#***---***---***---***---
#***---***---***---***---
#***---***---***---***---
#---***---***---***---***
#---***---***---***---***
#---***---***---***---***

cell_size = int(input("Enter the size: "))
rows = 8
cols = 8
for i in range(rows * cell_size):
    for j in range(cols * cell_size):
        if (i // cell_size + j // cell_size) % 2 == 0:
            print('*', end='')
        else:
            print('-', end='')
    print()

# Task_425

size = 9
stars = 0
spaces = 0
center = size // 2
choice = input("What figure do you want to display:\n Figure A\n Figure B\n Figure C\n Figure D\n Figure E\n Figure "
               "F\n Figure G\n Figure H\n Figure I\n Figure J\n For exit type: X\n")
while choice != "X":
    if choice == "A":
        for i in range(size):
            for j in range(size):
                if i <= size:
                    spaces = i
                    stars = size - i - 1
            print(" " * spaces + "*" * stars)
    if choice == "B":
        for i in range(size):
            for j in range(size):
                if i <= size:
                    stars = i
                    spaces = size - i - 1
            print("*" * stars + " " * spaces)
    if choice == "C":
        for i in range(size):
            for j in range(size, 0, -1):
                if i <= size:
                    stars = size - i - spaces
                    spaces = i
            print(" " * spaces + "*" * stars + " " * spaces)
    if choice == "D":
        for i in range(size, -1, -1):
            for j in range(size):
                if i <= size:
                    stars = size - i - spaces
                    spaces = i
            print(" " * spaces + "*" * stars + " " * spaces)
    if choice == "E":
        for i in range(size):
            for j in range(size):
                if i < center:
                    stars = size - i - spaces
                    spaces = i
                elif i > center and j > 5 or j < 9:
                    stars = 2 * (i - center) + 1
                    spaces = size - i - 1
            print(" " * spaces + "*" * stars + " " * spaces)
    if choice == "F":
        for i in range(size):
            for j in range(size):
                if i < center:
                    spaces = size - i - stars
                    stars = i
                elif i > center and j > 5 or j < 9:
                    spaces = 2 * (i - center) + 1
                    stars = size - i - 1
            print("*" * stars + " " * spaces + "*" * stars)
    if choice == "G":
        for i in range(size):
            for j in range(size):
                if i < center:
                    spaces = size - i - stars
                    stars = i
                elif i > center and j > 5 or j < 9:
                    spaces = 2 * (i - center) + 1
                    stars = size - i - 1
            print("*" * stars + " " * spaces)
    if choice == "H":
        for i in range(size):
            for j in range(size):
                if i < center:
                    spaces = size - i
                    stars = i
                elif i > center and j > 5 or j < 9:
                    spaces = i + 1
                    stars = size - i - 1
            print(" " * spaces + "*" * stars)
    if choice == "I":
        for i in range(size):
            for j in range(size):
                if i <= size:
                    stars = size - i - 1
                    spaces = i
            print("*" * stars + " " * spaces)
    if choice == "J":
        for i in range(size):
            for j in range(size):
                if i <= size:
                    spaces = size - i - 1
                    stars = i
            print(" " * spaces + "*" * stars)

    choise = input(
        "What figure do you want to display:\n Figure A\n Figure B\n Figure C\n Figure D\n Figure E\n Figure F\n "
        "Figure G\n Figure H\n Figure I\n Figure J\n For exit type: X\n")
