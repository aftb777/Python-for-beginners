# how to pass objects as arguements

class Car:
    
    color = None
    
class Motorcyle:
    
    color = None
    
def change_color(vehicle, color):
    
    vehicle.color = color
    
car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1 , "Red")
change_color(car_2 , "White")
change_color(car_3 , "Blue")

print(car_1.color)
print(car_2.color)
print(car_3.color)

bike_1 = Motorcyle()

change_color(bike_1 , "Green")

print(bike_1.color)