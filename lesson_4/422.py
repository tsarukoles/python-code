# Task_422

#***---***---***---***---
#***---***---***---***---
#***---***---***---***---
#---***---***---***---***
#---***---***---***---***
#---***---***---***---***

rows = 8
cols = 8
size = int(input("Enter the size of the cell: "))
for i in range(size):
    for j in range(size):
        if i == 0 and j == 4 or i == 1 and 3 <= j <= 5 or i == 2 and 2 <= j <= 6 or i == 3 and 1 <= j <= 7 or i == 4 and 0 <= j <= 9 or i == 5 and 1 <= j <= 7 or i == 6 and 2 <= j <= 6 or i == 7 and 3 <= j <= 5 or i == 8 and j == 4:
            print("*",end="")
        else:
            print(" ", end="")
    print()