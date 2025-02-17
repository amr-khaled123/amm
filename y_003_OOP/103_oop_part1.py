"""import qrcode
img = qrcode.make('كسم الصهاينة')
img.save('myqr001.png')
img.show()"""
# ----------------------------------------

# =================================
# == Object Oriented Programming ==
# =================================

"""class Employee:

    raise_amt = 1.04
    num_of_empo = 0

    def __init__(self, num, first_name, last_name, pay):
        self.num = num
        self.fname = first_name
        self.lname = last_name
        self.pay = pay
#        self.email=email

        Employee.num_of_empo += 1

    def full_name(self):
        print(f"{self.num}:{self.fname} {self.lname}")

    def apply_raise(self):
        return f"from employee {self.num}:{int(self.pay * self.raise_amt)}"

    @classmethod
    def set_raised_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_str(cls, emp_str):
        num, fname, lname, pay = emp_str.split('-')
        return cls(num, fname, lname, int(pay))

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return f"isn\'t work day"
        return f"it\'s work day"


print(Employee.num_of_empo)
employee_1 = Employee(1, "amr", "khaled", 4000)
employee_2 = Employee(2, "ahmed", "khaled", 5000)

emp_str_1 = '0-amr-khaled-2000'
new_emp_1 = Employee.from_str(emp_str_1)
print(new_emp_1.apply_raise())

print(employee_1.apply_raise())
print(employee_2.apply_raise())

print(Employee.raise_amt)
Employee.set_raised_amt(1.05)
print(Employee.raise_amt)

print(employee_1.apply_raise())
print(employee_2.apply_raise())
print(Employee.num_of_empo)

# date_time = datetime.date(2020, 11, 27)

# print(date_time.strftime("%A"))
# print(Employee.is_work_day(date_time))"""


"""class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        try:
            self.pay = int(pay)
        except ValueError:
            print("enter integer number")

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def apply_raise(self):
        return self.raise_amt*self.pay


class Developer(Employee):
    raise_amt = 1.05

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('==>', emp.fullname())


employee_1 = Employee("amr", "khaled", 5000)
employee_2 = Developer("ahmed", "mohamed", 5000, 'python')
mgr_1 = Manager("amr", "khaled", 5000, [employee_2, employee_1])
# print(help(Developer))
print(employee_1.apply_raise())
print(employee_2.apply_raise())
# mgr_1.add_emp(employee_1)
mgr_1.print_emps()
print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))"""


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.fulname = first+''+last
        self.email = self.fulname+"@gmail.com"
        try:
            self.pay = int(pay)
        except ValueError:
            print('enter integer number')

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def apply_raise(self):
        return self.raise_amt*self.pay

    def __repr__(self):
        return f"Employee('{self.fname}','{self.lname}','{self.pay}')"

    def __str__(self):
        return f"email of {self.fname}\\{self.email}"

    def __add__(self, other):
        return self.fname+other.fname


employee_1 = Employee('amr', 'khaled', 7000)
employee_2 = Employee('ahmed', 'mohamed', 5000)
# print(employee_1)
print(employee_1+employee_2)
print(repr(employee_1))
print(str(employee_1))


"""
class Developer(Employee):
    raise_amt = 1.05

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('==>', emp.fullname())


# employee_2 = Developer("ahmed", "mohamed", 5000, 'python')
# mgr_1 = Manager("amr", "khaled", 5000, [employee_2, employee_1])

# print(employee_1.__repr__())
# print(help(Developer))
# print(employee_1.apply_raise())
# print(employee_2.apply_raise())
# mgr_1.add_emp(employee_1)
# mgr_1.print_emps()
# print(isinstance(mgr_1, Developer))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Manager))
# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Employee))
"""
