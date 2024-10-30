# Task_424

#***---***---***---***---
#***---***---***---***---
#***---***---***---***---
#---***---***---***---***
#---***---***---***---***
#---***---***---***---***

cell_size = int(input("Enter the size: "))
rows = 8
cols = 8
for i in range(rows * cell_size):
    for j in range(cols * cell_size):
        if (i // cell_size + j // cell_size) % 2 == 0:
            print('*', end='')
        else:
            print('-', end='')
    print()