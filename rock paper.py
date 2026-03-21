# Create Rock paper scissor game

import random 

options = ("rock" , "paper" , 'scissor')
running = True

def new_func():
    return None

while running:
    
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter your choice : ")

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        print("its a tie")
        
    elif player == "rock" and computer == "scissors":
        print("You Won")
        

    elif player == "paper" and computer == "rock":
        print("You win")
        

    elif player == "scissors" and computer == "paper":
        print("You win")
        
    else:
        print("You lose")
        
    play_again = input("Play again? (y/n) : ").lower()
    if not play_again == "y":
        running = False
        
print()
print("Thanks for playing")