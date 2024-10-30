# Task_213

number=int(input("Enter the number: "))
if 100000 <= number <= 999999:
    a = number % 10  # 12345 6
    number //= 10  # 12345
    b = number % 10  # 1234 5
    number //= 10  # 1234
    c = number % 10  # 123 4
    number //= 10  # 123
    d = number % 10  # 12 3
    number //= 10  # 12
    e = number % 10  # 1 2
    number //= 10  # 1
    f = number + e + d
    g = c + b + a
    if f == g:
        print("Lucky number")
    else:
        print("No luck here!")
else:
    print("Invalid number")