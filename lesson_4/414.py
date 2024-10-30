# Task_414

amount = 0
for i in range(100, 10000):
    number = i
    numberFour = number % 10  #100 0
    number //= 10  #1000
    numberThree = number % 10  #10 0
    number //= 10  #100
    numberTwo = number % 10  #1 0
    number //= 10  #1
    if numberFour != numberThree and numberFour != numberTwo and numberFour != number and numberThree != numberTwo and numberThree != number and numberTwo != number:
        amount = amount + 1
print(amount)