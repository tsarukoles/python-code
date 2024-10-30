# Task_310

digits = 0
letters = 0
myStr = input("Enter a string: ")
for i in range(len(myStr)):
    if myStr[i].isdigit():
        digits += 1
    elif myStr[i].isalpha():
        letters += 1
print("Digits: ", digits, "Letters: ", letters)