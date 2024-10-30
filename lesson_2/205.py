# Task_205

seconds=int(input("Enter the amount of seconds: "))
print("1. Hours left:\n2. Minutes left:")
choice=int(input("Enter the choice: "))
if seconds<86400:
    if choice==1:
        print((86400-seconds)/3600)
    elif choice==2:
        print((86400-seconds)/60)
elif seconds>86400:
    print("More than a day")
else:
    print("Invalid option")