# Task_201

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
print("1. Sum of 2 numbers\n2. Difference of 2 numbers\n3. Average of 2 numbers\n4. Multiplication of 2 numbers")
option=int(input("Enter your option: "))
if option==1:
    print(first_number+second_number)
elif option==2:
    print(first_number-second_number)
elif option==3:
    print((first_number+second_number)/2)
elif option==4:
    print(first_number*second_number)
else:
    print("Invalid option")