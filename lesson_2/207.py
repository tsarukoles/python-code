# Task_207

cost_of_ps=int(input("Enter the cost of PS:"))
amount_bought=int(input("Enter the amount of PC bought:"))
discount_percentage=int(input("Enter the percentage amount:"))
selling_price=cost_of_ps-(((cost_of_ps/100)*discount_percentage))
print("1. Calculate the order total sum:\n2. Calculate the cost of 1 PC with discount:")
choice=int(input("Enter your choice:"))
if choice==1:
    print(amount_bought*selling_price)
elif choice==2:
    print(selling_price)
else:
    print("Invalid entry")