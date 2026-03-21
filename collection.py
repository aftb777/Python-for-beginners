# collection = single "variable" used to store multiple values
# lists = [] ordered and changeable. Duplicate OK
# set = {} unordered and immutable, but add/remove OK . No duplicates 
# tuple = () ordered and unchangeable. Duplicate OK. FASTER

#lists 

fruit = ["apple", "orange" , "banana" , "coconut"]

# NOTE : for all lists methods use 
# print(help(fruit))


# print(fruit[0])
# #we can do indexing operations with collections and also use loops with them

# for fruit in fruit:
#      print(fruit)
    
print(len(fruit))

print("apple" in fruit)
print("pineaplle" in fruit)

# fruit[0] = "pineapple"
# for fruit in fruit:
#      print(fruit)#now "apple" is replaced with "pineapple" 
     
fruit.insert(0, "mango")
print(fruit)

fruit.sort()#print lists in alphabetical order

print(fruit.index("apple"))

#Sets
#We cannot do indexing on the string

fruits = {"apple", "orange" , "banana" , "coconut"}

# NOTE : use this block of code to access all the sets methods
# print(dir(fruits))

#Tuple

fruitss = ("apple")
#print(dir(fruitss))