# Task_318

import re
expression = "12+34"
pattern = r'(\d+)([\+\-\*/])(\d+)'
match=re.match(pattern,expression)
if match:
    num1=int(match.group(1))
    op=match.group(2)
    num2=int(match.group(3))
    if op=='+':
        res=num1+num2
print(res)