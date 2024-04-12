# create a class programmer for storing information of few programmersworking at microsoft.


class Progammer:
    def information(self, name, age, company):
        self.company = company
        self.name = name
        self.age = age

    def printInfo(self):
        print(f"NAME OF THE CANDIDATE: {self.name} ")
        print(f"AGE OF THE {self.name}: {self.age} ")


amrit = Progammer()
amrit.name = "AMRIT DAJU"
amrit.age = 34
amrit.company = "GOOGLE"
amrit.information(amrit.name, amrit.age, amrit.company)
amrit.printInfo()
