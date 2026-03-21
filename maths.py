#Arithmatic operators
friends = 5
# friends = friends + 1 # Or friends += 1
friends *= 3
#friends -= 4
#friends /= 2
# friends = friends ** 2 # square
#modulus operators %
print(friends)

#Built in function
x = 3.14
y = -4
z = 5
result = round(x)
print(result)

result_y = abs(y)#print absoulute value
print(result_y)

solution = pow(4,3)#4x4x4
print(solution)

max_value = max(x,y,x)#gives maximum value
min_value = min(x,y,z)#gives minimum value
print(max_value)
print(min_value)

import math 
print(math.pi)
print(math.e)
square = math.sqrt(9)
print(square)

float1 = math.ceil(9.1)
float2 = math.floor(9.1)
print(float1)
print(float2)

#Exercise : circumference and area of circle 
radius = float(input("Enter the value of radius : "))
circumference = 2 * math.pi * radius
print(f"The circumference is : {round(circumference)}cm")

area_circle = math.pi * pow(radius,2)
print(f"The area of circle is {round(area_circle)}cm^2")

#Exercise hypotenuse of right angle triangle 
a = float(input("Enter the value of side A : "))
b = float(input("Enter the value of side B : "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The value of Hyptenuse is {c}")