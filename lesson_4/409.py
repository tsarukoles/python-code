# Task_409

useChoice=int(input("Enter what kind of currency you wnat to chage\n1-dollars to grn\n2-grn to dollars\n0- for exit"))

while useChoice!=0:
    amount = float(input("Enter how much money you will change: "))
    if useChoice==1:
        print("you will have",amount*41.5,"grn")
    elif useChoice==2:
        print("you will have",amount/41.5,"$")
    useChoice = int(
        input("Enter what kind of currency you wnat to chage\n1-dollars to grn\n2-grn to dollars\n0- for exit"))