# Task_214

number=int(input("Enter the number: "))
if 100000 <= number <= 999999:
    a = number % 10
    number //= 10
    b = number % 10
    number //= 10
    c = number % 10
    number //= 10
    d = number % 10
    number //= 10
    e = number % 10
    number //= 10
    print(a*100000+b*10000+d*1000+c*100+e*10+number)
else:
    print("Invalid number")