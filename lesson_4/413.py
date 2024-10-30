# Task_413

amount = 0
for i in range(100, 1000):
    number = i
    numberThree = number % 10  #10 0
    number //= 10  #10
    numberTwo = number % 10  #1 0
    number //= 10  #1
    if numberThree == numberTwo or numberThree == number or numberTwo == number:
        amount += 1
print(amount)