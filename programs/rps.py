# rock,paper, scissors program

import random 

options = ("rock","paper","scissors")

computer = options[random.randint(0,2)]

print("=====WELCOME TO THE GAME======")
player = input("Please enter Rock, Paper, or Scissors below:")

if player == computer:
    print("It's a tie.")
elif player == "rock":
    if computer == "paper":
        print("You lose, the computer wins")
    else:
        print("You win your opponent chose 'Scissors'")
elif player == "scissors":
    if computer == "rock":
        print("You lose! Your opponent chose 'Rock")
    else:
        print("You win! Your opponent chose 'Paper")
elif player == "paper":
    if computer == "rock":
        print("You Win! Your opponent chose 'Rock")
    else:
        print("You lose! Your opponent chose 'Scissors")
else: 
    print("Please enter a valid option.")
