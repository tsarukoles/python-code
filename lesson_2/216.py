# Task_216

number = int(input("Please, enter the number from 1-100:"))
if 1 <= number <= 100:
    if number % 5 == 0 and number % 3 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
else:
    print("Invalid entry")