# in this case child class becomes the parent class for another child class


# super method is used to access the methods of a super class in the derived class
 
class Person:
    country = "Nepal"
    city = "KATHMANDU"
    color = "dark"


class ChildOfPerrson(Person):
    color = "white"

    def lvlKnowledge(self):
        print(f"The lecel of knowledge is {self.knowledge}")


class CildOfChildOfPerrson(ChildOfPerrson):
    def lvlKnowledge(self):
        print(f"The lecel of knowledge is {self.knowledge}")


p = Person()
c1 = ChildOfPerrson()
c2 = CildOfChildOfPerrson()

print(f"{c1.country}")
print(f"{c2.country}")
