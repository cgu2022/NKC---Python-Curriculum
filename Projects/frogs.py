import random;
def move(frogList):
    # loop through the 3 frogs
    for i in range(0,3):
        # 50-50 chance of moving to the previous or next vertex.
        if(random.randint(0,1)):
            frogList[i] = (frogList[i] + 1) % 12
        else:
            frogList[i] = (frogList[i] - 1) % 12
def check(frogList):
    for i in range(0,3):
        for j in range(0,i):
            if(frogList[i] == frogList[j]):
                return False
    return True
def simulate(n):
    total = 0
    for i in range(0,n):
        # starting positions
        frogList = [0, 4, 8]
        moves = 0
        while(check(frogList)):
            move(frogList)
            moves += 1
        total += moves
    # average amount of time
    return total/n;
# main
print(simulate(100000))
