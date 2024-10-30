# Task_316

myList = []
mySum = 0
choice = input("Would you like to add to the list type: yes/no\n")
while choice != "no":
    if choice == "yes":
        myList.append(int(input("Enter a number: ")))
    choice = input("Would you like to add more: yes/no\n")
for i in myList:
    mySum += i
print(mySum)
print(mySum / len(myList))