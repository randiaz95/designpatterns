# Transports with Factory Method
# Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,
# but allows subclasses to alter the type of objects that will be created.
from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name, pointA, pointB):
        self.name = name
        self.pointA = pointA
        self.pointB = pointB

    def __str__(self):
        return f"{self.name} | {self.pointA} | {self.pointB}"
    
    @abstractmethod
    def move(self):
        pass


class Ship(Transport):
    def __init__(self):
        super().__init__("Ship")
        print("Creating a ship")
    
    def move(self):
        print("Sailing the ship")


class Truck(Transport):
    def __init__(self):
        super().__init__("Truck")
        print("Creating a truck")
    
    def move(self):
        print("Driving the truck")

class Rocket(Transport):
    def __init__(self):
        super().__init__("Rocket")
        print("Creating a rocket")
    
    def move(self):
        print("Flying the rocket")

if __name__ == "__main__":
    transport = Transport.create_transport("123", "456")
    transport.move()
    print(transport)