# Task_423

n=5
for i in range(2*n-1):
    if i<n:
        spaces=n-i-1
        stars=2*i+1
    else:
        spaces=i-n+1
        stars=2*(2*n-i-1)-1
    print(' '*spaces+'*'*stars)