class Employee:
    company = "NEA"
    salary = 9000
    salaryBonus = 700

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    # method name with @property decorator is called getter method
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary


e = Employee()
print(f"{e.totalSalary}")
e.totalSalary = 9006
print(e.salaryBonus)
