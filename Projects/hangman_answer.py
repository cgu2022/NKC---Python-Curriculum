import random

words = list()
picked = list()

def graphic(state): #0-5 for printing the hangman graphic
    graphic = (
        """
        *No Man :)*
        """,
        """
           0
        
        
        """,
        """
           0
           |
        
        """,
        """
           0
          -|
        
        """,
        """
           0
          -|-
        
        """,
        """
           0
          -|-
          /
        """,
        """
           0
          -|-
          / \\
        """,
    )
    print(graphic[state])


def collect():
    hold = ""
    while True:
        hold = input("Enter a word to add to the list, and enter \"play\" to start the game:").lower() #getting words
        if(hold in words):
            print("No repeats!")
            continue
        if hold=='play':
            if len(words)==0: #make sure there is at least one word in the list
                print("I'm sorry, but try again (you're list is empty):")
                continue
            else:
                break
        words.append(hold)

def game():
    if len(words)>0:
        ind = random.randint(0,len(words)-1) #pick a random word
        word = words[ind] #target word
        words.pop(ind)
    else: #if there are no more words to guess
        print("You tried all the words though!")
        return
    print("Game started and picked a word!")
    wordlen = len(word)
    tries = 6 #the amount of chances the player gets
    right = list() #store user guesses
    correct = 0 #keeps track of how many characters the player got correct

    while tries>0 and correct < wordlen: #while the user has chances and has not guessed the word
        print("Word: ") 
        for i in range(0, wordlen): #displaying the letters player got right so far
            if(word[i] in right):
                print(word[i],end=' ')
            else:
                print('_',end=' ')
        print("\n\nYou have guessed the following: \n", end=' ' ) #displaying what the user guessed already
        print(*right, sep = ", ") # the '*' is to prevent the [] from appearing when displaying the characters
        hold = ""
        while True: #make sure it is only 1 character and not already guessed
            hold = input("\nYou have: " + str(tries) + " left. Enter a character to guess: ").lower() #guessing part
            if len(hold)!=1:
                print('I\'m sorry, but only 1 character!')
            elif hold in right:
                print("You already guessed that!")
            else:
                break
        right.append(hold) #add the character to list of characters guessed
        if word.count(hold)>0: #got at least 1 character right
            correct+=word.count(hold)
            print("\n Nice Job! \n")
        else: #got no character(s) right
            tries-=1
            print("\n Rip \n")
        graphic(6-tries)
        print("\n\n\n")

    if correct==wordlen: #guessed word
        print("\nCongrats, you won! The word was: " + word)
    else: #ran out of guesses
        print("\nSorry :( , but the word was: " + word)
    print("\n\n\n\n\n")

def playagain():
    hold=""
    while hold!='Y' and hold!='N':
        hold = input("Would you like to play again? Y/N:").upper()
        if hold!='Y' and hold!='N':
            print("Sory, has to either be \"Y\" or \"N\"")
    if hold=='N':
        return False
    else:
        return True

def reset():
    hold = ""
    while hold!='Y' and hold!='N':
        hold = input("Would you like to reset the game?:").upper()
        if hold!='Y' and hold!='N':
            print("Sory, has to either be \"Y\" or \"N\"")
    if hold=='Y':
        words.clear()
        print("Resetted game!")
        return True
    else:
        return False

#driver
finished = True
collect()
while finished :
    game()
    finished = playagain()
    if finished:
        if reset():
            collect()
        
        

print("\n\tOkay, thanks for playing then!\n")

    