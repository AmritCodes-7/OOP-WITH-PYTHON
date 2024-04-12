class pet:  # creating a general class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def petHouse(self):
        print("NO HOUSE")


class cat(pet):  # inheriting the property of pet in cat
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def sound(self):
        print("MEOW")

    def petHouse(self):
        print("Bed")

    def show(self):
        print(
            f"I am {self.name} and I am {self.age} years old and color is {self.color}"
        )


class dog(pet):  # inheriting the property of pet in dog
    def sound(self):
        print("Bark")

    def petHouse(self):
        print("Shed")


class horse(pet):
    pass


c = cat("Mikey", 0.5, "Brown")
d = dog("Tommy", 2)
h = horse("Black", 5)
c.show()
d.show()
h.show()
c.petHouse()  # although same method is defined in the parent class it returns the method of child class
d.petHouse()
h.petHouse()  # this will return the parent class method as no sam emethod is defined in child class
