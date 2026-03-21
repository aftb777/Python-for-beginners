import random

# NOTE : print(help(random)) for all methods of random

# number = random.randint(1,20)
# print(number)

# low = 1
# high = 100
# num = random.randint(low , high)
# print(num)

#Exercise : Number guessing game

low = 1
high = 100
guesses = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}) : "))
    guesses += 1
    if guess < number:
        print(f"{guess} is too low")
    
    elif guess > number:
        print(f"{guess} is too high")
        
    else:
        print(f"{guess} is correct")
        break
    
print(f"this round took you {guesses} guesses")