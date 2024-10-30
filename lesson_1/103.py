#Task_103

a=int(input("Enter the number: "))
b=a%10
a //=10
c=a%10
a //=10
d=a%10
a //=10
e=b*1000+c*100+d*10+a
print(e)