# inheritacnce is a way of creating a new class from existing class


class Student:
    name = "AMRIT"

    def details(self):
        print("From jhapa")


class Amrit(Student):
    age = 18


all = Student()
me = Amrit()
print(me.name)
