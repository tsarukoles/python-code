# Test_507

def isLucky(num):
    b = num % 10  #12345 6
    num //= 10  #12345
    c = num % 10  #1234 5
    num //= 10
    d = num % 10  #123 4
    num //= 10
    e = num % 10  #12 3
    num //= 10
    f = num % 10  #1 2
    num //= 10
    if num + f + e == d + c + b:
        return "Lucky number"
    else:
        return "Not Lucky number"

print(isLucky(123456))
print(isLucky(123420))