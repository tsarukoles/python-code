# Task_218

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