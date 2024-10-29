// Task_1

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
print("1. Sum of 2 numbers\n2. Difference of 2 numbers\n3. Average of 2 numbers\n4. Multiplication of 2 numbers")
option=int(input("Enter your option: "))
if option==1:
    print(first_number+second_number)
elif option==2:
    print(first_number-second_number)
elif option==3:
    print((first_number+second_number)/2)
elif option==4:
    print(first_number*second_number)
else:
    print("Invalid option")

// Task_2

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
third_number=int(input("Enter the third number: "))
print("1. Sum of 3 numbers\n2. Multiplication of 3 numbers")
option=int(input("Enter your option: "))
if option==1:
    print(first_number+second_number+third_number)
elif option==2:
    print(first_number*second_number*third_number)
else:
    print("Invalid option")

// Task_3

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
third_number=int(input("Enter the third number: "))
print("1. Max of 3 numbers\n2. Min of 3 numbers\n3. Average of 3 numbers")
option=int(input("Enter the option: "))
if option==1:
    print(max(first_number,second_number,third_number))
elif option==2:
    print(min(first_number,second_number,third_number))
elif option==3:
    print((first_number+second_number+third_number)/2)
else:
    print("Invalid option")

// Task_4

meters=int(input("Enter the amount of meters: "))
print("1. Miles:\n2. Inches:\n3. Yards:")
choice=int(input("Enter your choice: "))
if choice==1:
    print(meters*0.00062137)
elif choice==2:
    print(meters*39.26)
elif choice==3:
    print(meters*1.0936)
else:
    print("Invalid choice")

// Task_5

seconds=int(input("Enter the amount of seconds: "))
print("1. Hours left:\n2. Minutes left:")
choice=int(input("Enter the choice: "))
if seconds<86400:
    if choice==1:
        print((86400-seconds)/3600)
    elif choice==2:
        print((86400-seconds)/60)
elif seconds>86400:
    print("More than a day")
else:
    print("Invalid option")

// Task_6

diameter=int(input("Enter the diameter of the circle:"))
print("1. Calculate the area of the circle\n2. Calculate the perimeter of the circle")
choice=int(input("Enter your choice:"))
if choice==1:
    print((3.141592653589793*0.25)*(diameter**2))
elif choice==2:
    print(diameter*3.141592653589793)
else:
    print("Invalid option")

// Task_7

cost_of_ps=int(input("Enter the cost of PS:"))
amount_bought=int(input("Enter the amount of PC bought:"))
discount_percentage=int(input("Enter the percentage amount:"))
selling_price=cost_of_ps-(((cost_of_ps/100)*discount_percentage))
print("1. Calculate the order total sum:\n2. Calculate the cost of 1 PC with discount:")
choice=int(input("Enter your choice:"))
if choice==1:
    print(amount_bought*selling_price)
elif choice==2:
    print(selling_price)
else:
    print("Invalid entry")

// Task_8

file_size = int(input("Enter the file size in GB:"))
internet_speed = int(input("Enter the internet speed:"))
file_size_bits = file_size*8*1024**3
download_time_seconds = file_size_bits/internet_speed
print("1.Downloading time - Hour:\n2. Downloading time - Minutes:\n3. Downloading time - Seconds:")
estimate_time = int(input("Please, enter Downloading time option:"))
if estimate_time == 1:
    print(int(download_time_seconds / 3600))
elif estimate_time == 2:
    print(int(download_time_seconds / 60))
elif estimate_time == 3:
    print(int(download_time_seconds))
else:
    print("Invalid data")

// Task_9

option=int(input("Please, enter the number for a day of the week:"))
if option == 1:
    print("Monday")
elif option == 2:
    print("Tuesday")
elif option == 3:
    print("Wednesday")
elif option == 4:
    print("Thursday")
elif option == 5:
    print("Friday")
elif option == 6:
    print("Saturday")
elif option == 7:
    print("Sunday")
else:
    print("Invalid option")

// Task_10

option=int(input("Please, enter the number for a day of the month:"))
if option == 1:
    print("January")
elif option == 2:
    print("February")
elif option == 3:
    print("March")
elif option == 4:
    print("April")
elif option == 5:
    print("May")
elif option == 6:
    print("June")
elif option == 7:
    print("July")
elif option == 8:
    print("August")
elif option == 9:
    print("September")
elif option == 10:
    print("October")
elif option == 11:
    print("November")
elif option == 12:
    print("December")
else:
    print("Invalid option")

// Task_11

option = int(input("Please, enter your number:"))
if option > 0:
    print("Number is positive!")
elif option < 0:
    print("Number is negative!")
elif option ==0:
    print("Number is equal to zero!")
else:
    print("Invalid entry")

// Task_12

first_number = int(input("Please, enter the first number:"))
second_number = int(input("Please, enter the second number:"))
if first_number == second_number:
    print("Numbers are equal")
elif first_number < second_number:
    print(first_number, second_number)
elif first_number > second_number:
    print(second_number, first_number)
else:
    print("Invalid entry!")

// Task_13

number=int(input("Enter the number: "))
if 100000 <= number <= 999999:
    a = number % 10  # 12345 6
    number //= 10  # 12345
    b = number % 10  # 1234 5
    number //= 10  # 1234
    c = number % 10  # 123 4
    number //= 10  # 123
    d = number % 10  # 12 3
    number //= 10  # 12
    e = number % 10  # 1 2
    number //= 10  # 1
    f = number + e + d
    g = c + b + a
    if f == g:
        print("Lucky number")
    else:
        print("No luck here!")
else:
    print("Invalid number")

// Task_14

number=int(input("Enter the number: "))
if 100000 <= number <= 999999:
    a = number % 10
    number //= 10
    b = number % 10
    number //= 10
    c = number % 10
    number //= 10
    d = number % 10
    number //= 10
    e = number % 10
    number //= 10
    print(a*100000+b*10000+d*1000+c*100+e*10+number)
else:
    print("Invalid number")

// Task_15

month = int(input("Please, enter the number from 1 to 12:"))
if 1 <= month <= 12:
    if 1 <= month <= 2 or month == 12:
        print("Winter")
    elif 3 <= month <= 5:
        print("Spring")
    elif 6 <= month <= 8:
        print("Summer")
    else:
        print("Autumn")
else:
    print("Invalid entry")

// Task_16

number = int(input("Please, enter the number from 1-100:"))
if 1 <= number <= 100:
    if number % 5 == 0 and number % 3 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
else:
    print("Invalid entry")

// Task_17

number = int(input("Please, enter the number:"))
power_of = int(input("Enter 'The power of' number:"))
if power_of==1:
    print(number)
elif power_of==2:
    print(number*number)
elif power_of==3:
    print(number*number*number)
else:
    print("Invalid entry")

// Task_18

salary_manager_one = 200
salary_manager_two = 200
salary_manager_three = 200
sales_manager_one = int(input("Sales for manager one:"))
sales_manager_two = int(input("Sales for manager two:"))
sales_manager_three = int(input("Sales for manager three:"))
if sales_manager_one < 500:
    salary_manager_one += sales_manager_one * 0.03
elif 500 <= sales_manager_one < 1000:
    salary_manager_one += sales_manager_one * 0.05
elif 1000 <= sales_manager_one:
    salary_manager_one += sales_manager_one * 0.08
if sales_manager_two < 500:
    salary_manager_two += sales_manager_two * 0.03
elif 500 <= sales_manager_two < 1000:
    salary_manager_two += sales_manager_two * 0.05
elif 1000 <= sales_manager_two:
    salary_manager_two += sales_manager_two * 0.08
if sales_manager_three < 500:
    salary_manager_three += sales_manager_three * 0.03
elif 500 <= sales_manager_three < 1000:
    salary_manager_three += sales_manager_three * 0.05
elif 1000 <= sales_manager_three:
    salary_manager_three += sales_manager_three * 0.08
if salary_manager_one > salary_manager_two and salary_manager_one > salary_manager_three:
    salary_manager_one += 200
elif salary_manager_two > salary_manager_one and salary_manager_two > salary_manager_three:
    salary_manager_two += 200
elif salary_manager_three > salary_manager_one and salary_manager_three > salary_manager_two:
    salary_manager_three += 200
print("The salary of the first manager is:", salary_manager_one)
print("The salary of the second manager is:", salary_manager_two)
print("The salary of the third manager is:", salary_manager_three)


