# Task_406

odd_five = 0
number_one = int(input("Enter the first number:"))
number_two = int(input("Enter the second number:"))
print("Range numbers:")
for i in range(number_one, number_two + 1):
    print(i)
    if i % 7 == 0:
        print("odd seven",i)
    if i%5==0:
        odd_five+=1
print("Range numbers in descending order:")
for number in range(number_two, number_one - 1, - 1):
    print(number)
print("count odd 5",odd_five)