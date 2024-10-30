# Task_302

import string

letters = 0
number = 0
myStr = input("Enter your text:")
for i in myStr:
    if i in string.ascii_letters:
        letters += 1
    if i in string.digits:
        number += 1
print(myStr)
print("Number of letters:", letters)
print("Number of numbers:", number)