# Task_203

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
third_number=int(input("Enter the third number: "))
print("1. Max of 3 numbers\n2. Min of 3 numbers\n3. Average of 3 numbers")
option=int(input("Enter the option: "))
if option==1:
    print(max(first_number,second_number,third_number))
elif option==2:
    print(min(first_number,second_number,third_number))
elif option==3:
    print((first_number+second_number+third_number)/2)
else:
    print("Invalid option")