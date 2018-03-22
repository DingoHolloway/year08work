# Need to be able to generate random numbers
import random

# Need somewhere to keep track of how many turns
turns = 0

# Need somewhere to keep score
scoreboard = 0

# Repeat this 10 times
while turns < 10 :

    # Computer Think of a number between 1 and 10
    number1 = random.randint(1,10)

    # Computer Think of a number between 1 and 10
    number2 = random.randint(1,10)

    # Ask the user what is number 1 + number 2
    print ("Question " + str(turns+1) + " - What is " + str(number1) + " + " + str(number2))

    # Check their answer
    answer = int(input(">>> "))

    if answer == (number1 + number2) :
    # If it's correct then add 1 to their score
        print("Well done, that's correct!")
        scoreboard = scoreboard + 1
    else:
    # If it's wrong then take 1 away from their score
        print("Too bad, that's not correct!")
        scoreboard = scoreboard - 1

    # Add 1 to the turn counter
    turns = turns + 1 


# Let them know the score
print("Your score is " + str(scoreboard))
