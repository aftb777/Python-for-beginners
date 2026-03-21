# name = input("Enter your name : ")
# age = float(input("Enter your age : "))

# print(f"Hello {name}")
# print(f"You are {age} years old")

#Exercise :mad libs
adjective1 = input("Enter first adjective :")
noun = input("Enter the noun : ")
adjective2 = input("Enter second adjective :")
verb = input("Enter the verb : ")
adjective3 = input("Enter third adjective :")

print(f"Today i went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

#Exercise : calculate area of rectangle
length = float(input("Enter the length of rectangle : "))
breadth = float(input("Enter the breadth of rectangle : "))
area = length * breadth
print(f"The area of rectangle is {area}cm^2")

#Exercise : shopping cart
item = input("What item were you like to buy : ")
price = float(input("What is the price : "))
quantity = int(input("How many you want to buy : "))

total = price * quantity 
print(f"You have bought a {quantity} x {item}/s")
print(f"Your total is : {round(total,2)}")
#round() is used to round off the value ,2 upto 2 numbers after decimal point 