from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)


# Turn that random number into the computer's RPS move
cGuess = ""
if (num == 1):
    cGuess = "rock"
elif (num == 2):
    cGuess = "paper"
elif(num == 3):
    cGuess = "scissors"

# Ask a user to enter their move
uGuess = (input("Enter your move ")) .lower()


# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("User Guess: ")
if (uGuess == "rock" ):
    print(rock)
elif (uGuess == "paper"):
    print(paper)
elif(uGuess == "scissors"):
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("Comp Guess: ")
if (cGuess == "rock" ):
    print(rock)
elif (cGuess == "paper"):
    print(paper)
elif(cGuess == "scissors"):
    print(scissors)

# Figure out who wins and print the result!
if ((cGuess == "scissors") and (uGuess == "rock" )) or ((uGuess == "scissors") and cGuess == "paper") or ((uGuess== "paper" and cGuess == "rock" )):
    print("User Wins!")
elif (uGuess == cGuess):
    print("That's a tie!")
else:
    print("Comp wins!!")
    
