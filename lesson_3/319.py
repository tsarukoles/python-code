expression = input("Enter a mathematical expression (e.g., 5+3): ")

op = ['+', '-', '*', '/']

for oper in op:
    if oper in expression:
        parts = expression.split(oper)
        num1 = int(parts[0])
        num2 = int(parts[1])

        if oper == '+':
            result = num1 + num2
        elif oper == '-':
            result = num1 - num2
        elif oper == '*':
            result = num1 * num2
        elif oper == '/':
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2

if 'result' in locals():
    print(f"The result of the expression '{expression}' is: {result}")
else:
    print("No valid operator found in the expression.")
