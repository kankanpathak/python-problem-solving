class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def accelerate(self, amount):
        self.__speed += amount

    def brake(self, amount):
        if self.__speed >= amount:
            self.__speed -= amount
        else:
            self.__speed = 0

    def display_info(self):
        return f"Brand: {self.brand}, Speed: {self.__speed}km/h"

class Car(Vehicle):
    def __init__(self, brand, model, speed):
        super().__init__(brand, speed)
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Speed: {self.get_speed()}km/h"


car = Car("Toyota", "Camry", 50)

car.accelerate(30)
car.brake(20)

print(car.display_info())
