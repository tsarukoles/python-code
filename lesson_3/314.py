# Task_314

digits = 0
symbols = 0
exclamations = 0
myStr = input("Enter a string: ")
choice = input("Enter your choice:\n1. Capital\n2. Digits\n3. Symbols\n4. Exclamations\n0. Exit\n")
myStrList = myStr.split()
while choice != 0:
    if choice == 1:
        print(myStr.title())
    elif choice == 2:
        for i in range(len(myStr)):
            if myStrList[i].isdigit():
                digits += 1
        print("Digits: ", digits)
    elif choice == 3:
        for i in range(len(myStr)):
            if myStrList[i] == "," or myStrList[i] == "." or myStrList[i] == "?" or myStrList[i] == ":" or myStrList[i] == ";":
                symbols += 1
        print("Symbols: ", symbols)
    elif choice == 4:
        for i in range(len(myStr)):
            if myStrList[i] == "!":
                exclamations += 1
        print("Exclamations: ", exclamations)
    choice = input("Enter your choice:\n1. Capital\n2. Digits\n3. Symbols\n4. Exclamations\n0. Exit\n")