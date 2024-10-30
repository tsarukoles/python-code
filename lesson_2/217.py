# Task_217

number = int(input("Please, enter the number:"))
power_of = int(input("Enter 'The power of' number:"))
if power_of==1:
    print(number)
elif power_of==2:
    print(number*number)
elif power_of==3:
    print(number*number*number)
else:
    print("Invalid entry")