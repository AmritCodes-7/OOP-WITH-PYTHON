class Employee:
    company = "Camel"
    salary = 900
    location = "nepal"

    # this will change the value of salary in the object we are  working in
    def changeSalary(self, sal):
        self.salary = sal

    # to change the value of the salary from the class itself
    def changeSalary2(self, sal):
        self.__class__.salary = sal

    # or
    @classmethod
    def changeSalary3(cls, sal):
        cls.salary = sal


e = Employee()
# e.changeSalary(908)
# e.changeSalary2(908)
e.changeSalary3(908)
# print(f"{e.salary}")
print(Employee.salary)
