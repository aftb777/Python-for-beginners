# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA" : "Washington DC",
            "India" : "New Delhi",
            "Russia" : "Moscow",
            "China" : "Beijing"}

# NOTE : print(help(capitals)) for dictionary methods

print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capitals exists")
    
else:
    print("That capital doesnt exists")

if capitals.get("Russia"):
    print("That capital exists")
    
else:
    print("That capital doesnt exists")
    
capitals.update({"Germany": "Berlin"})
print(capitals)

for key, value in capitals.items():
    print(f"{key} : {value}")