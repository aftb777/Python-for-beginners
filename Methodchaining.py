# Method chaining = calling multiple methods sequentially
#                   each cell performs an action on the same  object and returns self

class Car:
    
    def turn_on(self):
        print("You start Engine")
        return self   # Always do this while method chaining
        
    def drive(self):
        print("You drive the car")
        return self
        
    def brake(self):
        print("You step on the breaks")
        return self
        
    def turn_off(self):
        print("You turn off the engine")
        return self
        
car = Car()

car.turn_on().drive().brake().turn_off()  # Method chaining 

print() 
#Another way of method overriding
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()