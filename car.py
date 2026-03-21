class Car:
    
    wheels = 4  # class variable (initialised outside contructor)
        
    def __init__(self,make,model,year,color):   #constructor
    
        self.make = make        #instance variables
        self.model = model       #instance variables
        self.year = year         #instance variables
        self.color = color       #instance variables
        
    def drive(self):
        print(f"This {self.model} is driving")
        
    def stop(self):
        print(f"This {self.model} has stopped")