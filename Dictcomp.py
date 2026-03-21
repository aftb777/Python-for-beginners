# Dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# Syntax:
# dictionary ={key : expression for (key,value) in iteration}
# dictionary ={key : expression for (key,value) in iteration if conditional}
# dictionary = {key : (if/else) for (key,value) in iterable}
# dictionary = {key : function(value) for (key,value) in iterable}

cities_in_F = {'New york' : 32 , 'Boston' : 75 , "Los angeles" : 100 , "chicago" : 50}
# this are temperature of cities i farehniet


cities_in_C = {key : round((value - 32) * (5/9)) for (key,value) in cities_in_F.items()} # if value >= 50 
print(cities_in_C)

print()

desc_cities = {key : ("Warm" if value >= 40 else "Cold") for (key,value) in cities_in_F.items()}
print(desc_cities)

print()

def check_temp(value):
    if value >= 70:
        return "hot" 
    else:
        return "cold"
    
desc1_cities = {key : check_temp(value) for (key,value) in cities_in_F.items()}
print(desc1_cities)