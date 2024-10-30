# Test_504

def maxNum(a, b, c, d):
    result = a

    if b > result:
        result = b
    if c > result:
        result = c
    if d > result:
        result = d
    return result

result = maxNum(1, 2, 21, 4)
print(result)