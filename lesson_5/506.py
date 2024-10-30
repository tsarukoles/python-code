# Test_506

def isSimpleNumber(num):
    if num <2:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    sqrt_num=int(num **0.5)+1
    for i in range(3,sqrt_num,2):
        if num%i==0:
            return False
    return True

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(isSimpleNumber(5))
print(isSimpleNumber(2))
print(isSimpleNumber(10.1))
print(isSimpleNumber(-9))