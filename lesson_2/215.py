# Task_215

month = int(input("Please, enter the number from 1 to 12:"))
if 1 <= month <= 12:
    if 1 <= month <= 2 or month == 12:
        print("Winter")
    elif 3 <= month <= 5:
        print("Spring")
    elif 6 <= month <= 8:
        print("Summer")
    else:
        print("Autumn")
else:
    print("Invalid entry")