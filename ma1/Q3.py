# Q.3- Using the function basic salary from Question 1, write another function gross salary that calculates the gross salary of an employee. This function should accept basic salary as input (output from Question 1), consider a fixed value of allowances (e.g., 20% of basic salary), and return the gross salary (basic salary + allowances - tax).

from Q2 import tax_amount

def gross_salary(basic_salary):
    allowances = basic_salary * 0.20
    tax = tax_amount(basic_salary)
    gross = basic_salary + allowances - tax
    return gross

basic = int(input("Enter basic salary: "))
print("Gross Salary:", gross_salary(basic))



# Output:
# Enter basic salary: 80000
# Gross Salary: 84000.0