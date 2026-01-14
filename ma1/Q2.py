# Q.2- Create a function tax amount that shows how much taxes are deducted from the basic salary. Taxes are applied as follows:
# • If the salary is less than Rs. 60,000/-, deduct 10% as tax.
# • If the salary is between Rs. 60,000/- and Rs. 85,000/-, deduct 15% as tax.
# • If the salary is more than Rs. 85,000/-, deduct 20% as tax

def tax_amount(basic_salary):
    if basic_salary < 60000:
        tax = basic_salary * 0.10
    elif 60000 <= basic_salary <= 85000:
        tax = basic_salary * 0.15
    else:
        tax = basic_salary * 0.20
    return tax

basic = int(input("Enter basic salary: "))
print("Tax Amount:", tax_amount(basic))



# Output:
# Enter basic salary: 75000
# Tax Amount: 11250.0