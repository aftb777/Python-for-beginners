#Format specifiers = {:flags} format a value based on what flags are inserted

#Used in context of f string

#Flags 
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces 
# :03 = allocate and zero pad that may spaces
# :< = left justify
# :> = right justify
# :^ = centre align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers 
# :, = comma operator gives commas between standard units like 1,000 or 10,00,000

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.3f}")#Take 3 digits only after decimal point
print(f"Price 2 is {price2:.2f}")#Take 2 digits only after decimal point
print(f"Price 3 is {price3:.1f}")#Take 1 digits only after decimal point

print(f"Price 1 is {price1:10}")#Give 10 spaces 

print(f"Price 1 is {price1:010}")#pad with zero

#NOTE : we can perform multiple flags on indexes