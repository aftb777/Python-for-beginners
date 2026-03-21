#typecasting = the process of converting a value of one data type to another data type
#              (string, float, integer, boolean)
#              Imlicit vs Explicit

#Explicit
name = "Bro"
age = 18
gpa = 1.9
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

student = str(student)
print(student)
print(type(student))

name = bool(name)
print(name)

#Implicit
x = 3
y = 3.0
x = x/y
print(x)#now x is converted to float