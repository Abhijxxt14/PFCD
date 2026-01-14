# Q.4- Using the gross salary function from Question 3, write a function salary bracket that categorizes the employee’s gross salary into one of the following brackets:
# • ”Low income” if gross salary is below Rs. 50,000/-.
# • ”Middle income” if gross salary is between Rs. 50,000/- and Rs. 80,000/-.
# • ”High income” if gross salary is more than Rs. 80,000/-

from Q3 import gross_salary

def salary_bracket(basic_salary):
    gross = gross_salary(basic_salary)
    if gross < 50000:
        return "Low income"
    elif 50000 <= gross <= 80000:
        return "Middle income"
    else:
        return "High income"

gross = int(input("Enter gross salary: "))
print("Salary Bracket:", salary_bracket(gross))



# Output:
# Enter basic salary: 80000
# Gross Salary: 84000.0
# Enter gross salary: 84000
# Salary Bracket: High income