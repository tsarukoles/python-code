# Task_419

start = int(input("Enter a start number: : "))
end = int(input("Enter an end number: "))

print("Numbers", start, "to", end, ":")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')