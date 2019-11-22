# Emmet Houghton
# May 14, 2019
# This program allows 2 players to play Tic-Tac-Toe in the terminal.

# Needed to pick who goes first
import random as rand

# Main function containing the loop for the program - calls initiation functions for setup and then 
    # enters loop that iterates each turn
def main():
    # Welcome the users and create the board
    print("Welcome to Tic-Tac-Toe")
    table = create_board()

    # Get user information using function
    player1, player2, symbol1, symbol2 = get_user_info()

    # Pick a random player to go first
    randomizer = rand.randint(1, 2)
    currentPlayer = ""
    if randomizer == 1:
        currentPlayer = player1
        currentSymbol = symbol1
    else:
        currentPlayer = player2
        currentSymbol = symbol2
    
    # Print the original state of the game
    print_board(table)

    # Enter the game loop
    gameRunning = True
    while gameRunning:      
        # Get choice from user
        choice = get_valid_input(table, currentPlayer)

        # Place the player's symbol in the table
        place_choice(table, choice, currentSymbol)

        # Swap which player is up - keeps track of who is going and which symbol is theirs
        if currentPlayer == player1:
            currentPlayer = player2
            currentSymbol = symbol2
        else:
            currentPlayer = player1
            currentSymbol = symbol1
        
        # Print the current state of the game
        print_board(table)

        # Check if the game is over, and end the game + congratulate winner accordinly
        winCondition = game_is_over(table, symbol1, symbol2)
        # Player 1 won
        if winCondition == 1:
            congratulate_winner(player1)
            gameRunning = False
        # Player 2 won
        if winCondition == 2:
            congratulate_winner(player2)
            gameRunning = False
        # Tie game
        if winCondition == 3:
            congratulate_winner(player1, player2)
            gameRunning = False

# Create the board of any size between 3 and 9 for the players to play on
def create_board():
    table = []
    invalid = True

    # Make sure they enter valid size
    while invalid:
        size = input("What size would you like your board? (Enter 1 dimension): ")
        try:
            size = int(size)
            # Capping sizes at 3x3 and 9x9 for practicality (and the fact that aligning 3 digit numbers
            # would not look as good haha) - the program still would work though because functions
            # would run for infinite sized board
            if 10 > size > 2:
                invalid = False
                # Clarify rules for larger boards
                if size > 3:
                    print("NOTE: For a board larger than 3x3, you must fill an entire row, column,\
 or diagonal to win.")
                
                # Loop through rows to create the multidimentional array
                i = 1
                for row in range(0, size):
                    table.append([])
                    for column in range(0, size):
                        # Avoiding error line lol
                        column = column
                        table[row].append(str(i))
                        i += 1
                return table
            else:
                print("Please input a size between 3 and 9. Try again.")
        # Handle case where they input a string for size
        except ValueError:
            print("Invalid input for size! Please try again")

# Prints the current state of the board for players to see throughout the game
def print_board(table):
    # Print a new line
    print()
    # Loop through each item in each row, printing as it goes
    for row in table:
        for slot in range(0, len(row)):
            # Print bar thingy if not first thing in row
            if slot != 0:
                print("|", end = " ")
    
            # Print the entry
            print(row[slot], end = " ")
            
            # Print an extra space if it's 1 digit or a symbol in a larger board
            # because some entries are 2 digits (to keep things aligned)
            if len(table) > 3 and len(str(row[slot])) == 1:
                print(" ", end = "")
        
        # Return to next line
        print()
    # Print another new line for aesthetics
    print()

# Gets names and symbols of the players
def get_user_info():
    # Get their names
    player1 = get_valid_name(1)
    player2 = get_valid_name(2)

    # Make sure it is a valid symbol
    symbol1 = get_valid_symbol(player1)
    # Make sure symbol is valid, but also check that it is not the same as player1's symbol
    symbol2 = get_valid_symbol(player2, symbol1)
    
    return player1, player2, symbol1, symbol2

# Get the column and row of any given choice in the table (works for all sizes)
def get_slot(table, choice):
    # Calculate row and column based on size of table
    length = len(table)
    row = (choice - 1) // length
    column = (choice - 1) % length
    # Return coordinates
    return row, column

# Places choice in its corresponding location for any square matrix
def place_choice(table, choice, symbol):
    # Get the correct slot and then place the symbol in the table
    row, column = get_slot(table, choice)
    table[row][column] = symbol

    return table

# Makes sure that the slot that the player chose is not already taken
def slot_is_taken(table, choice):
    row, column = get_slot(table, choice)
    # Checks to see if the spot is occupied by a symbol
    if table[row][column].isdigit():
        return False
    return True

# Function that gets the player's name - This is needed to make sure that it is at least 1 char long
    # because the congrats function relies on their name not being nothing
def get_valid_name(numPlayer):
    invalid = True
    name = ""

    # Keep asking player1/2 until they provide a valid name
    while invalid:
        if numPlayer == 1:
            name = input("Player 1, enter your name: ")
        elif numPlayer == 2:
            name = input("Player 2, enter your name: ")
        
        if len(name) > 0:
            invalid = False
        else:
            print("Please enter a name at least 1 character long!")

    # Return the name
    return name

# Gets a player's symbol and makes sure that a symbol is 1 char long and not a number
# If you pass the optional parameter it will also check that the chosen symbol is not the same as the
# optional parameter
def get_valid_symbol(player, symbol1 = ""):
    validSymbol = False

    # Keep asking until a valid symbol is entered
    while not validSymbol:
        print(player, end = ", ")
        symbol = input("please enter the symbol/letter you want to use: ")
        # Run all of the checks to see if it is valid. If not, loop through and try again
        if not symbol.isdigit() and len(symbol) == 1 and symbol != symbol1:
            validSymbol = True
        else:
            print("You have entered an invalid symbol! Try again.")

    # Return the valid symbol
    return symbol
            
# Gets input that is valid, not chosen already, and within the range of the table
def get_valid_input(table, player):
    valid = False
    num = 0

    while not valid:
        # Asks the correct player where they want to go
        print(player, end = ", ")
        num = input("enter your choice: ")
        
        # Tests for all invalid cases (see below comments)
        try:
            num = int(num)
            # Makes sure it is within the range of the table
            if (len(table)**2 + 1) > num > 0 :
                # Makes sure that the slot is not already taken
                if not slot_is_taken(table, num):
                    valid = True
                else:
                    print("That slot has already been chosen! Try again.")
            else:
                print("Your selection is out of the range of the table!")
        # Handle exception for string input
        except ValueError:
            print("Your choice is invalid. Please try again.")

    # Return the valid input
    return num

# Checks if the game is over by calling the following 2 functions (rows/columns and diagonals)
# Also checks to see if the game is tied
# Returns 0 for nothing (keep checking), 1 for player1 win, 2 for player2 win, and 3 for a tie
def game_is_over(table, symbol1, symbol2):
    
    # Check northwest to southeast diagonal - return winner if there is one, but keep checking if not
    diagonal1 = check_diagonal(table, symbol1, symbol2, "southeast")
    if diagonal1 != 0:
        return diagonal1
    
    # Check northeast to southwest diagonal - return winner if there is one, but keep checking if not
    diagonal2 = check_diagonal(table, symbol1, symbol2, "southwest")
    if diagonal2 != 0:
        return diagonal2

    # Check rows for a winner - return winner or a tie if present, keep checking if not
    row = check_rows_columns_tie(table, symbol1, symbol2, "row")
    if row != 0:
        return row
    
    # Checks columns for winner - return winner if present, if not return that the game is not over
    column = check_rows_columns_tie(table, symbol1, symbol2, "column")
    if column != 0:
        return column
    
    # Return here is the game is not over
    return 0

# Checks for a winner in rows and columns - I made these in the same function because they share a lot
    # of the same code...
# Returns same thing as game_is_over(): 0 for nothing, 1 for player1 wins, 2 for player2, 3 for tie
def check_rows_columns_tie(table, symbol1, symbol2, direction):        
    tieGame = True
    
    # Loop through columns/rows for correct amount of times based on size of table
    for i in range(0, len(table)):
        threeInARow = True

        # Compare with row 1 for columns, column 1 for rows (basically gets where the row/column)
            # is starting
        firstSlot = ""
        if direction == "row":
            firstSlot = table[i][0]
        if direction == "column":
            firstSlot = table[0][i]

        # Loop through the other dimension of the board (which one depends on if it is rows or columns)
        for j in range(0, len(table)):
            slot = ""
            # Get the current slot of the row/column (each one has to be retrieved inversely)
            if direction == "row":
                slot = table[i][j]
            if direction == "column":
                slot = table[j][i]
            
            # Check to see if it disqualifies the row/column from being a winning row
            if slot != firstSlot:
                threeInARow = False
            # Check to see if it disqualifies the game from being a tie (if it's a digit)
            if slot != symbol1 and slot != symbol2:
                tieGame = False
        
        # If there was a winner in the row/column, check who it was
        if threeInARow:
            if firstSlot == symbol1:
                return 1
            if firstSlot == symbol2:
                return 2
    
    # If the function still has not found a number after checks, return tie, if not return negative
    if tieGame:
        return 3
    else:
        return 0

# Does not have to check for tie because it is checked for in rows and columns
# Optional parameter "backward" is set to true if you want to check northeast to southwest
    # (It normally checks northwest to southeast)
def check_diagonal(table, symbol1, symbol2, direction):
    threeInARow = True
    
    # Get the first slot in the diagonal to compare it to other slots
    firstSlot = ""
    if direction == "southwest":
        firstSlot = table[0][len(table)-1]
    elif direction == "southeast":
        firstSlot = table[0][0]

    # Loop through the list, while increasing slot number in each list if going forwards, decreasing
    # if backwards
    for i in range(0, len(table)):
        slot = ""
        if direction == "southwest":
            j = 2 - i
            slot = table[j][i]
        elif direction == "southeast":
            slot = table[i][i] 
        
        # If it finds a discrepancy, the diagonal cannot be a win condition
        if slot != firstSlot:
            threeInARow = False

    # Return 0 for no winer, 1 for player 1 wins, and 2 for player 2 wins. No need to check for ties
        # because the rows and columns function checks for ties (it is much easier that way because rows and
        # columns check every item in the board while diagonals do not)
    if threeInARow:
        # If there is a winner, check who it was
        if firstSlot == symbol1:
            return 1
        if firstSlot == symbol2:
            return 2
    else:
        return 0

# Just a function to say congrats to the winner :D - if it gets passed 2 players it will say they tied
def congratulate_winner(player, player2 = ""):
    if player2 == "":
        print("Congratulations to the winner, " + str(player) + "!")
    else:
        print(player, "and", player2, "have tied!")
    
# Call the main function and start the game
main()