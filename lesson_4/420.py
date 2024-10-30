# Task_420

numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
for i in range(numberOne, numberTwo + 1):
    for j in range(1, 10 + 1):
        print(i, "*", j, "=", i * j, end="\t")
    print()