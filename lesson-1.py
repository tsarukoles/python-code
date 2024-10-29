//Task_1

a=int(input("Enter the number: "))
b=a%10
a //=10
c=a%10
a //=10
d=a%10
a //=10
f=a*d*c*b
print(f)

//Task_2

a=int(input("Enter the length in meters: "))
b=a*100
c=a*10
d=a*1000
e=a*0.000621371
print(a,"m = sm",b)
print(a,"m = dm",c)
print(a,"m = mm",d)
print(a,"m = miles",e)

//Task_3

a=int(input("Enter the number: "))
b=a%10
a //=10
c=a%10
a //=10
d=a%10
a //=10
e=b*1000+c*100+d*10+a
print(e)

//Task_4

a=int(input("Enter the high of the triangle:"))
b=int(input("Enter the base of the triangle:"))
c=(a*b)/2
print("The area of the triangle is ",c)

c=int(input("Please, enter a number: "))
if c%2==0:
    print("Even number")
else:
    print("Odd number")

//Task_5

number=int(input("Enter a number: "))
if number%7==0:
    print(number,"Number is multiple of 7")
else:
    print(number,"Number is not multiple of 7")
