# Q.5- Take three different sets of employee names, hourly rates and hours worked per week as user input. Write a Python function employee report that generates a formatted report of all employees’ salary details. This function should print the employee names, basic salaries, gross salaries, tax amounts, and salary brackets in a readable format.

from Q1 import total_salary
from Q2 import tax_amount
from Q3 import gross_salary
from Q4 import salary_bracket

def employee_report():
    for i in range(3):
        name = input(f"Enter name for employee {i+1}: ")
        hourly_rate = float(input(f"Enter hourly rate for {name}: "))
        hours_worked = float(input(f"Enter hours worked per week for {name}: "))

        basic = total_salary(hourly_rate, hours_worked)
        gross = gross_salary(basic)
        tax = tax_amount(gross)
        bracket = salary_bracket(gross)

        print(f"\nEmployee Report for {name}:")
        print(f"Basic Salary: {basic}")
        print(f"Gross Salary: {gross}")
        print(f"Tax Amount: {tax}")
        print(f"Salary Bracket: {bracket}")

print(employee_report())



# Output:
# Enter hourly rate: 400
# Enter hours worked per week: 45
# Basic Salary: 64000
# Overtime Salary: 12000.0
# Total Salary: 76000.0

# Enter basic salary: 64000
# Tax Amount: 9600.0
# Gross Salary: 67200.0

# Enter gross salary: 67200
# Salary Bracket: Middle income

# Enter name for employee 1: Hari
# Enter hourly rate for Hari: 300
# Enter hours worked per week for Hari: 40

# Employee Report for Hari:
# Basic Salary: 48000.0
# Gross Salary: 52800.0
# Tax Amount: 5280.0
# Salary Bracket: Middle income

# Enter name for employee 2: Luci
# Enter hourly rate for Luci: 900
# Enter hours worked per week for Luci: 50

# Employee Report for Luci:
# Basic Salary: 198000.0
# Gross Salary: 198000.0
# Tax Amount: 39600.0
# Salary Bracket: High income

# Enter name for employee 3: Ramesh 
# Enter hourly rate for Ramesh: 100
# Enter hours worked per week for Ramesh: 30

# Employee Report for Ramesh:
# Basic Salary: 12000.0
# Gross Salary: 13200.0
# Tax Amount: 1320.0
# Salary Bracket: Low income
