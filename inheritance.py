# class Animal:#parent functions
    
#     alive = True
    
#     def eat(self):
#         print("This animal is eating")  
          
#     def sleep(self):
#         print("This animal is sleeping")
        
# class Rabbit(Animal):#Rabbit is child class and animal is parent class
#     def run(self):
#         print("This rabbit is running")

# class Fish(Animal):#child function
#     def swim(self):
#         print("This fish is swimming")

# class Hawk(Animal):#child function
#      def fly(self):
#          print("This hawk is flying")

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

# print()

# rabbit.run()
# fish.swim()
# hawk.fly()

# Multi level Inheritance

# when a derived (child) class inherits another derived (child) class

# class Organism: # Parent class
    
#     alive = True
    
# class Animal(Organism): # Inherit from organism
    
#     def eat(self):
#         print("This animal is eating")
        
# class Dog(Animal): # derived child class from Animal
    
#     def bark(self):
#         print("This dog is barking")
        
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()


# Multiple Inheritance = when a child class is derived from more than one parent class

# class Prey:
    
#     def flee(self):
#         print("The animal flees")
        
# class Predator:
    
#     def hunt(self):
#         print("This animal is Hunting")
        
# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey , Predator):
#     pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()


# Method overriding

class Animal:
    
    def eat(self):
        print("This animal is Eating")
        
class Rabbit(Animal):
    
    def eat(self):
        print("This rabbit is eating a carrot")
    
    
rabbit = Rabbit()
rabbit.eat()# It will print child class not parent class (bcoz it closest)

#This is called overriding in PYTHON 