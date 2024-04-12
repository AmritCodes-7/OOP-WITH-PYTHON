class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getname(self):
        return self.name

amrit = Person("Amrit Tamang", 30)
print(amrit.getname())
        