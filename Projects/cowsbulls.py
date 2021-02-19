# used for generating a random number.
import random

# this function returns a list:
# the first element is the number of cows, the second element is the number of bulls
def compare_numbers(number, user_guess):
    cowbull = [0,0] #cows, then bulls
    for i in range(len(number)):
        # if the digit matches, add one to the number of cows.
        if number[i] == user_guess[i]:
            cowbull[0]+=1
        # if the digit does not match, add one to the number of bulls.
        else:
            cowbull[1]+=1
    return cowbull

isPlaying = True # start by playing the game.
randomNumber = str(random.randint(1000,9999)) # random 4 digit number.
numGuesses = 0 # keeps track of the number of guesses.

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls.")
print("Type exit at any prompt to exit.")

# loops until the user quits or guesses the correct number.
while isPlaying:
    user_guess = input("Give me your best guess! ")
    if(user_guess == "exit"): # user wants to quit
        break
    elif(len(user_guess) != 4): # invalid guess
        print("Your guess must be 4 digits long.")
    else: # the guess is valid
        cowbullcount = compare_numbers(randomNumber,user_guess)
        numGuesses += 1 # increment the number of guesses.
        print("You have " + str(cowbullcount[0]) + " cows and " + str(cowbullcount[1]) + " bulls.")
        if cowbullcount[0]==4:
            isPlaying = False # stop playing the game because the user won.
            print("You win the game after " + str(numGuesses) + " guesses! The number was " + str(randomNumber) + ".")
        else:
            print("Your guess isn't quite right, try again.")
