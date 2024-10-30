# Test_511

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