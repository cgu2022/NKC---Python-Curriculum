import random

words = []
picked_word = ""
picked_word_chars = []

tries = 6
correct = 0
won = False
guessed_letters = []


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

def collect_words():
	entered_word = ""
	while entered_word != "play":
		entered_word = input("Enter a word to add to the list or enter \"play\" to start the game: ").lower()
		if entered_word in words:
			print("Already entered that word. Try entering a different word.")
		elif entered_word == "play":
			if len(words) == 0:
				print("Your word list is empty. Add more words.")
		else:
			words.append(entered_word)

def pick_random_word():
	global picked_word # need global when modifying variable outside function
	index = random.randint(0, len(words)-1)
	picked_word = words.pop(index)
	
def create_blanks():
	word_length = len(picked_word)
	for i in range(0, word_length):
		picked_word_chars.append("_")

def print_guess():
	word = ""
	for c in picked_word_chars:
		word += c + " "
	print(word)

def find_all_matches(letter):
	match_indexes = []
	for i in range(0, len(picked_word)):
		if picked_word[i:i+1] == letter:
			match_indexes.append(i)
	return match_indexes

def win_check():
	if correct == len(picked_word):
		return True
	else:
		return False

def info_graphic():
	print_guess()
	graphic(6-tries)
	letter_print_out = ""
	for i in guessed_letters:
		letter_print_out += i + ", "
	print(letter_print_out)

def guess_letter():
	letter = ""
	while letter == "" or letter in guessed_letters:
		letter = input("Guess a letter:").lower()
		if letter in guessed_letters:
			print("You already guessed {}".format(letter))
	guessed_letters.append(letter)

	return letter

def correctness_check(letter):
	global correct, won, tries
	letter_matches = find_all_matches(letter)
	if len(letter_matches) != 0:
		print("correct")
		for i in letter_matches:
			picked_word_chars[i] = letter
		correct += len(letter_matches)
		won = win_check()
	else:
		print("wrong")
		if letter not in guessed_letters:
			guessed_letters.append(letter)
		tries -= 1
	
def play():
	info_graphic()
	while tries > 0 and not won:
		guessed_letter = guess_letter()
		correctness_check(guessed_letter)
		info_graphic()
		print("{} tries remaining".format(tries))
	if won:
		print("You won!")
	else:
		print("You lost!")
		print("The correct word was \"{}\"".format(picked_word))
	#play_again_prompt() #challenge

def play_again_prompt():
	answer = input("Play again? (Y, N): ")
	if answer == "Y":
		play_again()
	elif answer == "N":
		print("Thanks for playing!")

def play_again():
	global tries, correct, won, guessed_letters, picked_word_chars
	if len(words) == 0:
		answer = input("0 words left. Can't play again. Would you like to add more words? (Y, N)")
		if answer == "Y":
			collect_words()
			tries = 6
			correct = 0
			won = False
			guessed_letters = []
			picked_word_chars = []
			pick_random_word()
			create_blanks()
			play()
		elif answer == "N":
			print("Thanks for playing!")
	else:
		tries = 6
		correct = 0
		won = False
		guessed_letters = []
		picked_word_chars = []
		pick_random_word()
		create_blanks()
		play()


collect_words()
pick_random_word()
create_blanks()
play()
