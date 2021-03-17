# function to find the length of a hailstone sequence starting at n.
def hailstone(n):
    seqLength = 1
    while(n != 1):
        # if n is odd, n = 3n+1
        if(n % 2 == 1):
            n = 3*n+1
        # if n is even, n = n/2
        else:
            n = n/2
        # increment the length of the sequence
        seqLength += 1
    return seqLength
# slightly better efficiency
def betterHailstone(n, list):
    # base case
    if(n == 1):
        list[1] = 1
        return 1
    else:
        if(n % 2 == 1):
            if(3*n+1 < len(list)):
                if(list[3*n+1] != 0):
                    return 1 + list[3*n+1]
                else:
                    # storing the length in the list
                    list[3*n+1] = betterHailstone(3*n+1, list)
                    return 1 + betterHailstone(3*n+1, list)
            else:
                return 1 + betterHailstone(3*n+1, list)
        else:
            if(n/2 < len(list)):
                if(list[n/2] != 0):
                    return 1 + list[n/2]
                else:
                    # storing the length in the list
                    list[n/2] = betterHailstone(n/2, list)
                    return 1 + list[n/2]
            else:
                return 1 + betterHailstone(n/2, list)
# main
maxIndex = -1
maxLength = 0
for i in range(1, 1000001):
    length = hailstone(i)
    if(length > maxLength):
        maxIndex = i
        maxLength = length
print("First method:")
print("Sequence starting with " + str(maxIndex) + " has length " + str(maxLength))
# slightly faster version below
mI = -1
mL = 0
list = []
for j in range(0, 1000001):
    list.append(0)
for k in range(1, 1000001):
    l = betterHailstone(k, list)
    if(l > mL):
        mI = k
        mL = l
print("Second method:")
print("Sequence starting with " + str(mI) + " has length " + str(mL))
