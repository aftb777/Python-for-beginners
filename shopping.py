#shopping cart program 

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (press Q to quit) : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food} : "))
        foods.append(foods)
        prices.append(prices)

print(f"----- YOUR CART -----")

for food in foods:
    print(food , end = " ")
    
for price in prices:
    total += price
    
print()
print(f"Your total is : {total}")