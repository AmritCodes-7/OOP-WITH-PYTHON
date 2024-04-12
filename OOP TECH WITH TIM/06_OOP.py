class person:
    no_of_person = 0 # class attribute

    def __init__(self, name):
        self.name = name
        person.no_of_person += 1  # using class attribute
        

p1 = person("amrit")
p1 = person("amrit")
print(p1.no_of_person) 
        
