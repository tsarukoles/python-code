# Task_418

width = int(input("Enter the width:"))
height = int(input("Enter the height:"))
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()