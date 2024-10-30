# Task_212

first_number = int(input("Please, enter the first number:"))
second_number = int(input("Please, enter the second number:"))
if first_number == second_number:
    print("Numbers are equal")
elif first_number < second_number:
    print(first_number, second_number)
elif first_number > second_number:
    print(second_number, first_number)
else:
    print("Invalid entry!")