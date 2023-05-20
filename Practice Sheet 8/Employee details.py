"Write a Python class Employee with attributes like emp_id, emp_name, emp_salary,
and emp_department and methods like calculate_emp_salary,
emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
● Use 'assign_department' method to change the department of an employee.
● Use 'print_employee_details' method to print the details of an employee.
● Use 'calculate_emp_salary' method takes two arguments: salary and
hours_worked, which is the number of hours worked by the employee. If the
number of hours worked is more than 50, the method computes overtime and
adds it to the salary. Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))"
class Employee:
    emp_id=0
    emp_name=''
    emp_salary=0
    emp_department=0
    hours_worked=0
    def __init__(self,emp_id,emp_name,emp_salary,emp_department,hours_worked):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        self.hours_worked=hours_worked
    def calculate_emp_salary(self,salary,hour_worked):
        if self.hours_worked<50:
            return (self.emp_salary==self.emp_salary)
        else:
            self.emp_salary=((self.hours_worked-50)*(salary/50))
            return self.emp_salary
    def emp_assign_department(self,dep):
        self.emp_department=dep
        return self.emp_department
    def print_employee_details(self):
        return self.emp_id, self.emp_name, self.emp_salary, self.emp_department
e1=Employee(int(input('Entre Employee_Id =')),input('Entre Employee Name ='),int(input('Employee salary =')),input('Employee department ='),int(input('Hours worked =')))
print(e1.print_employee_details())
print(e1.calculate_emp_salary(int(input('Salary =')),int(input('Hours worked ='))))
print(e1.emp_assign_department(input('Enter department to assign =')))
print(e1.print_employee_details())

