class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def update_salary(self,new_salary):
        self.update_salary = (new_salary * 1.10)


employee_1 = Employee("John",5000)


print(employee_1.name + "'s", " salary is: ", employee_1.salary, "\n")


employee_1.update_salary(5000)


print("John's new salary is after his raise: ", employee_1.update_salary)

