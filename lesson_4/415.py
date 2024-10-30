# Task_415

result = 0
decimal = 1
number = int(input("Enter a number: "))
while number != 0:
    if number%10!=3 and number%10!=6:
        result+=number%10*decimal
        decimal*=10
    number//=10
print(result)
number = input()
result = ""
for i in number:
    if i != "3" and i != "6":
        result += i

print(result)