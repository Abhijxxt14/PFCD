# Q.1- Write a Python function basic_salary that accepts two parameters: hourly_rate and hours_worked_per_week. The function should calculate the basic salary per month (assuming a month has 4 weeks). If the hours worked per week exceed 40, create another function overtime_salary, where every extra hour worked is paid at 1.5 times the normal hourly rate. Finally, create another function total_salary that returns the sum of the basic salary and overtime. worked per week exceed 40, create another function overtime_salary, where every extra hour worked is paid at 1.5 times the normal hourly rate. Finally, create another function total_salary that returns the sum of the basic salary and overtime.

def basic_salary(hourly_rate, hours_worked_per_week):
    if hours_worked_per_week <= 40:
        return hourly_rate * hours_worked_per_week * 4
    else:
        return hourly_rate * 40 * 4
    
def overtime_salary(hourly_rate, hours_worked_per_week):
    if hours_worked_per_week > 40:
        overtime_hours = hours_worked_per_week - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5 * 4
        return overtime_pay
    else:
        return 0
    
def total_salary(hourly_rate, hours_worked_per_week):
    basic = basic_salary(hourly_rate, hours_worked_per_week)
    overtime = overtime_salary(hourly_rate, hours_worked_per_week)
    return basic + overtime

hourly_rate = int(input("Enter hourly rate: "))
hours_worked_per_week = int(input("Enter hours worked per week: "))
print("Basic Salary:", basic_salary(hourly_rate, hours_worked_per_week))
print("Overtime Salary:", overtime_salary(hourly_rate, hours_worked_per_week))
print("Total Salary:", total_salary(hourly_rate, hours_worked_per_week))



# Output:
# Enter hourly rate: 400
# Enter hours worked per week: 45
# Basic Salary: 64000
# Overtime Salary: 12000.0
# Total Salary: 76000.0