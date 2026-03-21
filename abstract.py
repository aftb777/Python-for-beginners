# Prevents the user from creating an object of that class
# compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods 
# abstract methods = a method that has a declaration but does not have implementation

from abc import ABC , abstractmethod

class Vehicle(ABC): 
    
    @abstractmethod # Now our vehicle class is abstract class
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    
    def go(self):
        print("You ride the Car")
        
    def stop(self):
        print("This car is stopped")
        
class Motorcycle(Vehicle):
    
    def go(self):
        print("You ride the motorcycle")
        
    def stop(self):
        print("This Motorcycle is stopped")
        
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

print()

car.stop()
motorcycle.stop()