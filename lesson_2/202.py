# Task_202

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
third_number=int(input("Enter the third number: "))
print("1. Sum of 3 numbers\n2. Multiplication of 3 numbers")
option=int(input("Enter your option: "))
if option==1:
    print(first_number+second_number+third_number)
elif option==2:
    print(first_number*second_number*third_number)
else:
    print("Invalid option")