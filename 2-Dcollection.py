# fruits = ["apple" , "orange" , "banana" , "coconut"]
# vegetables = ["celery" , "carrots" , "potatoes"]
# meats = ["chicken" , "fish" , "turkey"]

# groceries = [fruits , vegetables , meats]

# print(groceries[0][0])#print apple it means 0th row 0th column
# print(groceries[0])#print first row

#second way

groceries =[["apple" , "orange" , "banana" , "coconut"],
            ["celery" , "carrots" , "potatoes"],
            ["chicken" , "fish" , "turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()
    
#same operation we can do on tuple set
#we can also make nested collections