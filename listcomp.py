# list comprehension = a way to create a new list with less syntx 
#                    can mimic certain lambda functions , easier to read 
# Syntaxes :
#                    list = [expression for item in iterate]
#                    list = [expression for item in iterable if condition]
#                    list = [expression if/else for item in iterable]

squares = [] # create an empty list
for i in range(1,11): # create a loop
    squares.append(i * i) # define each loopniteration should do
print(squares)

# by list comprehension method

squares = [i * i for i in range (1,11)]
print(squares)

print()

students = [100,90,80,70,60,50,40,30,20,10,0]

# pased_students = [i for i in students if i >= 60]
pased_students = [i if i >= 60 else "failed" for i in students]

print(pased_students)