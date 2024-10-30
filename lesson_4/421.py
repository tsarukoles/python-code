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