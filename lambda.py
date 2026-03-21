# lambda function = function written in 1 line using lambda keyword 
#                   accepts any number of arguements but only has one expression 
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

# Lambda parameters : expression

double = lambda x : x * 2
print(double(4))

multiply = lambda x , y : x * y
print(multiply(3,5))

full = lambda first_name, last_name : first_name + " " + last_name
print(full("Bro" , "Code"))

age = lambda age :  True if age >= 18 else False
print(age(21))