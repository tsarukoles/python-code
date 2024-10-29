// Test_1

//“Don’t let the noise of others’ opinions
//drown out your own inner voice.”
//Steve Jobs

def myFormText():
    print('“Don’t let the noise of others\ndrown out you own inner voice’\nSteve Jobs')
myFormText()

// Test_2

def myNumber(a,b):
    for i in range(a,b+1): # using cycle, a and b+1 become a range fom 1 - 10
        if i%2 == 0:
            print(i)

myNumber(1, 10)

// Test_3

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

// Test_4

def maxNum(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    elif b > c and b > a and b > d:
        return b
    elif c > a and c > b and c > d:
        return c
    elif d > a and d > b and d > c:
        return d

result = a

if b > result:
    result = b
if c > result:
    result = c
if d > result:
    result = d

print(result)


maxNum(1, 2, 21, 4)

// Test_5

def sumNumbers(a, b):
    mySum = 0
    for i in range(a, b + 1):
        mySum += i
    return mySum


print(sumNumbers(1, 5))


// Test_6

def isSimpleNumber(num):
    if num <2:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    sqrt_num=int(num **0.5)+1
    for i in range(3,sqrt_num,2):
        if num%i==0:
            return False
    return True

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


print(isSimpleNumber(5))
print(isSimpleNumber(2))
print(isSimpleNumber(10.1))
print(isSimpleNumber(-9))

// Test_7

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

// Test_8

def isEven(numOne, numTwo):
    for i in range(numOne, numTwo + 1):
        if i % 2 == 0:
            print(i)


isEven(1, 20)


// Test_9

def whatSquare(length, symbol, logic):
    if logic == True:
        for i in range(length):
            for j in range(length):
               print(symbol, end="\t")
            print()
    elif logic == False:
        for i in range(length):
            for j in range(length):
                if i == 0 or i == length - 1 or j == 0 or j == length - 1:
                    print(symbol, end="\t")
                else:
                    print(" ", end="\t")
            print()




whatSquare(5,"*", False)
print()
whatSquare(5,"*", True)


// Test_10

def minNum(a, b, c, d, e):

    if a > b and a > c and a > d and a > e:
        return a
    elif b > c and b > a and b > d and b > e:
        return b
    elif c > a and c > b and c > d and c > e:
        return c
    elif d > a and d > b and d > c and d > e:
        return d
    elif e > a and e > b and e > c and e > d:
        return e

print(minNum(1, 2, 3, 4, 5))
print(minNum(6, 2, 3, 4, 5))


// Test_11

def multiplyNum(a, b):

    if b < a:
        a, b = b, a # Other way (only in Python)
        # tmp = a
        # a = b
        # b = tmp
    result = 1
    for i in range(a, b + 1):
        result *= i

    return result


print(multiplyNum(1, 5))
print(multiplyNum(5, 1))


// Test_12

def amountNum(number):
    result = 0
    while number != 0:
        number //= 10
        result += 1
    return result


print(amountNum(104234230))

// Test_13

def myPalindrome(number):

    reversePalindrome = []
    isPalindrome = []

    for i in range(number):

        while number != 0:
            a = number % 10
            reversePalindrome.append(a)
            number //= 10

    for i in reversePalindrome:
        isPalindrome.append(i)

    print(reversePalindrome)
    print(isPalindrome)




print(myPalindrome(123))

