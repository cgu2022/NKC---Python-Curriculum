# 2d array.
board=[['_','_','_'],['_','_','_'],['_','_','_']]
# This function checks if we have won.
def checkWin():
    for i in range(0,3):
        # Checking for 3 in a row.
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]!='_':
            return True
        # Checking for 3 in a column.
        elif board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]!='_':
            return True
        # Checking for diagonals.
        elif board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!='_':
            return True
        elif board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0]!='_':
            return True
        elif checkTie():
            return True
    return False

# This function checks for a tie.
def checkTie():
    for i in range(0,3):
        # Checking if there are spaces left.
        for j in range(0,3):
            if(board[i][j]=='_'):
                return False
    return True

# This functions just prints the board.
def printBoard():
    print(board[2])
    print(board[1])
    print(board[0])

# player keeps track of whose turn it is.
player=0
print("Welcome to Tic-tac-toe...")
printBoard()

# The loop keeps running while we haven't won or tied.
while not checkWin() and not checkTie():
    # user input
    a=input("Player "+str(player+1)+": (x-coordinate,y-coordinate) ")
    a=str(a)
    # We check to make sure that the user input is valid.
    if(int(a[4])>3 or int(a[4]<0) or int(a[1])>3 or int(a[1])<0):
        print("Illegal move!")
        # This will alternate the players.
        # The players will be alternated again later, so the same player will go again if there is an illegal move.
        player=(player+1)%2
    elif (board[int(a[4])-1][int(a[1])-1])=='_':
        # player 1 is 'o'
        if player==0:
            board[int(a[4])-1][int(a[1])-1]='o'
        # player 2 is 'x'
        if player==1:
            board[int(a[4])-1][int(a[1])-1]='x'
    else:
        print("Illegal move!")
        # The players will be alternated again later, so the same player will go again if there is an illegal move.
        player=(player+1)%2
    # This will alternate the players.
    player=(player+1)%2
    printBoard()

# Here, we have finished the loop, so we determine the winner.
if checkTie():
    print("Tie!")
else:
    # The player who last played won.
    print("Player "+str((player+1)%2+1)+" wins!")
