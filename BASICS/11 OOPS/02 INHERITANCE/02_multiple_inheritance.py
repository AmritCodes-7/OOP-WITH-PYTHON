class Employee:
    company = "google"

    def printing(self):
        print("hey this is me")


class FreeLancer:
    company = "FIVERr"
    level = 0

    def upgradeLevel(self):
        self.level += 1


class Programmer(Employee, FreeLancer):
    name = "don"


amrit = Programmer()
print(f"{amrit.level}")
print("AFTER UPGRADE")
amrit.upgradeLevel()
print(f"{amrit.name} is of level {amrit.level}")
print(f"{amrit.company}") #since both the class has company as class attributes but the priority will be given to the first parent class

