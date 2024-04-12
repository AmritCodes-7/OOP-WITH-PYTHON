# self is not compulsory we can use any other word too 
class Bus:
    def __init__(self, name, fare, seats) -> None:
        self.name = name
        self.fare = fare
        self.seats = seats

    def busInfo(self):
        print("\n")
        print(f"The Bus you are currently looking is {self.name}")
        print(f"Fare from {self.location} to {self.destination} is Rs {self.fare}.")

    def customerRoute(self, location, destination):
        self.location = location
        self.destination = destination
        print("\n")
        print(f"Currently your location is {self.location}")
        print(f"Your destination would be {self.destination}.")

    def busStatus(self):
        print("\n")
        print(f"No. of seats available is {self.seats}")

    def bookTicket(self):
        print("\n")
        if self.seats > 0:
            print(f"Your ticket from {self.location} to {self.destination} is booked.")
            self.seats = self.seats - 1
        else:
            print(f"SEAT FULL !!! SORRY")
    
    def cancelTicket(self):
        pass



location = input("Enter your location: ")
destination = input("Enter your destination: ")

cl_bus = Bus(f"{destination} EXPRESS", 500, 39)
cl_bus.location = location
cl_bus.destination = destination
cl_bus.customerRoute(cl_bus.location, cl_bus.destination)
cl_bus.busInfo()
cl_bus.bookTicket()
cl_bus.busStatus()