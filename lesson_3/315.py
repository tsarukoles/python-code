# Task_315

myList = []
choice = input("Would you like to add to the list type: yes/no\n")
while choice != "no":
    if choice == "yes":
        myList.append(int(input("Enter a number: ")))
    choice = input("Would you like to add more: yes/no\n")
myFind = int(input("Enter a number to find:"))
result = myList.count(myFind)
print(myList)
print(result)