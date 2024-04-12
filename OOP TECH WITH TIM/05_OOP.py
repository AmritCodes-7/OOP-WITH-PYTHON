class person:
    no_of_person = 0 # class attribute

    def __init__(self, name):
        self.name = name
        

p1 = person("amrit")
p1.no_of_person = 2 # instance attribute 
print(p1.no_of_person) # since instacne attribute's preference is more than class attribute so it prints 2
        
