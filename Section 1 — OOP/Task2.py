from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stoped")

    def fuel_type(self):
        print("Petrol")

class Bike(Vehicle):
    def start(self):
        print("Bike Started")

    def stop(self):
        print("Stoped")

    def fuel_type(self):
        print("Petrol")

class Tesla(Vehicle):
    def start(self):
        print("Tesla Started")

    def stop(self):
        print("Tesla Stoped")

    def fuel_type(self):
        print("Electricity")

c=Car()
c.start()
c.stop()
c.fuel_type()

b=Bike()
b.start()
b.stop()
b.fuel_type()

t=Tesla()
t.start()
t.stop()
t.fuel_type()