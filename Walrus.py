# walrus operator :-

# new to python 3.8
# assignment expression aka walrus operator
# Assigns values to variable as a part of a larger expression 

happy = True
print(happy)# Output : True

# print(happy = True) # It will throw error instead of this use walrus operator

print(happy := True)


# foods = list()
# while True:
#     food = input("What food do you like ? : " )
#     if food == "quit":
#         break
#     foods.append(food)

# writing the same program using walrus operator

foods = list()
while food := input("What food do you like? : ") != "quit":
    foods.append(food)