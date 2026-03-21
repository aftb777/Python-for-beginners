# super() = Function used to give access to the methods of a parent class
#           Returns a temporary object of a parent class when used

class Rectangle:
      
    def __init__(self , length , width): #We have made a function here
        self.length = length
        self.width = width 

class Square(Rectangle):
    
    def __init__(self , length , width):
       super().__init__(length , width)  # recall it here using super()  
       
    def area(self):
        return self.length * self.width
        
class Cube(Rectangle):
    
    def __init__(self , length , width , height):
       super().__init__(length , width) # recall it here using super()  
       self.height = height
       
    def volume(self):
        return self.length * self.width * self.height
        
square = Square (3 , 3)
cube = Cube(3 ,3 , 3)

print()
print(square.area())
print(cube.volume())