# Test_503

def myLine(a, b, c):
    if b == "v":
        for i in range(a):
            print(c)

    elif b == "h":
        print(c*a)

length = int(input("Enter the length of your line: "))
direction = input("Enter your direction: ")
symbol = input("Enter your symbol: ")

myLine(length, direction, symbol)