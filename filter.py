#filter() : creates a collection of elements from an iterable for which a function returns

# filter(function , iterable)

friends = [("Rachael" , 19) , 
           ("Monica" , 18) , 
           ("Phoebe" , 17) , 
           ("joey" , 16) , 
           ("Chandler" , 20) , 
           ("Ross" , 21)]

# create a list of 18+ friends

age = lambda data : data[1] > 18

drink_list = list(filter(age , friends))

for i in drink_list:
    print(i)