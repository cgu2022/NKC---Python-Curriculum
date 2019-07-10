#######################################################################################
# Hangman Wikipedia link: https://en.wikipedia.org/wiki/Hangman_(game)
# Hangman is a game where the player tries to guess a specific word with the least 
# number of wrong guesses as possible. On each guess, the player guesses a letter 
# he/she thinks is part of the word. If he guesses correct, it is added to the list of 
# correct words. If not, then the one part of the skeleton is drawn. When the whole 
# skeleton is drawn, the player loses, but if the player gets all the letters right, 
# he wins. Before every guess, the player gets to see the letters he has gotten right, 
# all the guesses he/she has made, the state of the skeleton, and the letters he guessed 
# can be seen in the word like so:  _ p p _ e.

# Write a program which continually prompts the player to enter words to store in the 
# computer (you should use a list to do this) until the player enters the string “play”.
# The program must have at least one word stored. Then, the game will choose a random word 
# out of the list of words entered for the player to guess. The “play” entered to initiate 
# the game will not appear in the list of possible words to choose from. Before each guess, 
# display the state of the skeleton, display the “_ p _ _ _,” the letters the player has 
# guessed, and number of guesses the player has left. In this program, the player will have 
# 6 tries before the player loses. If the player loses, display the word the computer chose. 
# And for each guess, the player will enter a character. If the player inputs anything else 
# besides a character, or a character the player has already guessed, make sure to tell 
# him/her that and re-prompt until he gets it right. Once the player enters the guess, 
# make sure to let him know whether he got it right or wrong, and then do the whole cycle 
# again until the game ends. Once the game ends, after telling the player either a win 
# or loss, ask the player if he wants to play again (Y/N). If no, simply display 
# “Thanks for playing!” If yes, ask the player if he wants to reset the game. If yes, 
# clear the whole list of words the computer can choose from and redo the whole thing 
# (from the beginning of this paragraph). If no, make sure to not re-choose any words the 
# player already entered. If there are no more words to choose from, tell him that, 
# and like before, go all the way back to the beginning of the program.

# This is probably the largest program you will have writen so far. Remember to do easy things first
# and make a solid framework, then try to tackle the whole problem altogether.
# This is not an easy problem - so if you get frustrated, don't worry and keep going!
# Good Luck!

#By Chris G