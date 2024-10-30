# Test_510

def minNum(a, b, c, d, e):

    if a > b and a > c and a > d and a > e:
        return a
    elif b > c and b > a and b > d and b > e:
        return b
    elif c > a and c > b and c > d and c > e:
        return c
    elif d > a and d > b and d > c and d > e:
        return d
    elif e > a and e > b and e > c and e > d:
        return e

print(minNum(1, 2, 3, 4, 5))
print(minNum(6, 2, 3, 4, 5))