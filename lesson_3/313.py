# Task_313

myStr = input("Enter a string: ")
myFind = input("Enter a search word: ")
myChange = input("Enter a change word: ")
myStrList = myStr.split()
for i in range(len(myStrList)):
    if myStrList[i] == myFind:
        myStrList[i] = myChange
result = " ".join(myStrList)
print(result)