from abc import ABC, abstractmethod


class CarFactory(ABC):
    @abstractmethod
    def createCar(self):
        pass
    
    @abstractmethod
    def carSpecification(self):
        pass

class NorthAmericanCarFactory(CarFactory):
    def createCar(self):
        return Sedan()
    
    def carSpecification(self):
        return NorthAmericanSpecification()


class EuropeanCarFactory(CarFactory):
    def createCar(self):
        return ElectricHatchback()
    
    def carSpecification(self):
        return EuropeanSpecification()

class Car(ABC):
    @abstractmethod
    def assemble(self):
        pass

class CarSpecification(ABC):
    @abstractmethod
    def display(self):
        pass

class Sedan(Car):
    def assemble(self):
        print("Assembling Sedan car.")

class ElectricHatchback(Car):
    def assemble(self):
        print("Assembling Hatchback car.")

class NorthAmericanSpecification(CarSpecification):
    def display(self):
        print("North American Specification: Requires Turn signals you don't use.")

class EuropeanSpecification(CarSpecification):
    def display(self):
        print("European Specification: Requires flammable electric batteries.")


if __name__ == "__main__":
    factories = []
    factories.append(NorthAmericanCarFactory())
    factories.append(EuropeanCarFactory())

    # All factories make compatible products
    # The client code may or may not know the concrete classes
    for factory in factories:
        car = factory.createCar()
        car.assemble()
        spec = factory.carSpecification()
        print(car, spec)
        