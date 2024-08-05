# Builder is a creational design pattern that lets you construct complex objects step by step.
# The pattern allows you to produce different types and representations of an object using the same construction code.
# Not needed in python because we can set param to None in python and not need to have many constructor methods.
class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def build(self):
        return self.car


class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.color = None
        self.engine = None

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Engine: {self.engine}"


# Usage example
car = CarBuilder()\
        .set_brand("Tesla")\
        .set_model("Model 3")\
        .set_color("Red")\
        .set_engine("Electric")\
        .build()

print(car)