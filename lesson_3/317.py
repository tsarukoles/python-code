# Task_317

expression = input("Enter your expression or exit with X: ")
while expression != "X" and expression != "x":
    for operator in ['+', '-', '*', '/']:
        if operator in expression:
            left, right = expression.split(operator)
            left = float(left.strip())
            right = float(right.strip())
            if operator == '+':
                result = left + right
            elif operator == '-':
                result = left - right
            elif operator == '*':
                result = left * right
            elif operator == '/':
                if right != 0:
                    result = left / right
                else:
                    result = "Invalid division"
            print("Result:", result)
    expression = input("Enter your expression or exit with X: ")
print("Exit")
expression=input()
result=eval(expression)
print(result)