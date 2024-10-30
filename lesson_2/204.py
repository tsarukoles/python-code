# Task_204

meters=int(input("Enter the amount of meters: "))
print("1. Miles:\n2. Inches:\n3. Yards:")
choice=int(input("Enter your choice: "))
if choice==1:
    print(meters*0.00062137)
elif choice==2:
    print(meters*39.26)
elif choice==3:
    print(meters*1.0936)
else:
    print("Invalid choice")