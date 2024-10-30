# Task_412

x = int(input("Enter numer X: "))
y = int(input("Enter number Y: "))
pow = x
for i in range(y):
    pow *= x
print(pow)

for i in range(1,10):
    for j in range(1,10):
        print(i*j,end="\t")
    print()