# Task_403

number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))
while number_one < number_two:
    number_one += 1
    if number_one % 2 == 1:
        continue
    print(number_one)