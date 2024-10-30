# Test_512

def amountNum(number):
    result = 0
    while number != 0:
        number //= 10
        result += 1
    return result

print(amountNum(104234230))