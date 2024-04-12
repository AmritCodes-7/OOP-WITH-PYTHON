class vehicle:
    def __init__(self, color_of_car, age_of_car, seats_of_car):
        self.color = color_of_car
        self.age = age_of_car
        self.seat = seats_of_car

    def get_color(self):
        return f"The color of the car is {self.color}"

    def get_life(self):
        return f"The remaining life of the car on the road is {20 - self.age}"


mycar = vehicle("black", 1, 5)
print(mycar.get_color())
print(mycar.get_life())
