#Logical operator = used on conditional stattements

# and = checks 2 or more condition if true
# or = checks if at least one condition is true
# not = true if codition is false, and vice versa

temp = 25
sunny = False
if temp > 0 or temp < 30:
    print('The temp is good')
else :
    print("The temperature is bad")
    
if not sunny:
    print("It is sunny outside") 
    
else :
    print("It is cloudy outside")