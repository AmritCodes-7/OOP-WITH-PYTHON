class Dog:  # creating a class

    # learning init function
    def __init__(self, name):
        self.name = name
        # print(name)

    def bark(self):  # creating a method
        print("Bark")

    def add_one(self, x):  # method takes the parameter x and returns a value by adding 1
        return x + 1


tommy = Dog("Tommy")  # creating an object of class Dog
tommy.bark()  # calling the method of class Dog
print(tommy.add_one(1))
