# Task_307

myStr = input("Enter your text:")
myRes = input("Enter reserved words:")
myList = myRes.split()
myStrList = myStr.split()
for word in range(len(myStrList)):
    if myStrList[word] in myList:
        myStrList[word] = myStrList[word].upper()
result = " ".join(myStrList)
print(result)