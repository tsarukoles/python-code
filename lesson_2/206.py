# Task_206

diameter=int(input("Enter the diameter of the circle:"))
print("1. Calculate the area of the circle\n2. Calculate the perimeter of the circle")
choice=int(input("Enter your choice:"))
if choice==1:
    print((3.141592653589793*0.25)*(diameter**2))
elif choice==2:
    print(diameter*3.141592653589793)
else:
    print("Invalid option")