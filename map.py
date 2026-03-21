# map() = applies a function to each item in an iterable (list , tuple etc)

# map(fuction , iterable)

# Converting dollars into Euros

store = [("Shirt" , 20.00) , 
         ("Pants" , 25.00) , 
         ("Jackets" , 50.00) , 
         ("Socks" , 10.00)]

to_euros = lambda data : (data[0] , data[1] * 0.82)
to_dollars = lambda data : (data[0] , data[1] / 0.82)

store_euros = list(map(to_euros , store))
store_dollars = list(map(to_dollars, store))

for i in store_euros:
    print(i)
    
print()

for x in store_dollars:
    print(x)