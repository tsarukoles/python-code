# Task_405

number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))
for number_one in range(number_one - 1, number_two):
    number_one += 1
    if number_one % 2 == 0:
        continue
    print(number_one)