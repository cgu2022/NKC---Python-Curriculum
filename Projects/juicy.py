# This function returns the divisors of n in a list.
def listDivisors(n):
    divisors = []
    for i in range(1,n+1):
        if(n%i==0):
            divisors.append(i)
    return divisors

# This function checks if n is juicy or not.
def checkJuicy(n):
    divisors = listDivisors(n)
    for i in range(1, len(divisors)):
        k = divisors[i]-divisors[i-1]
        if(n%k!=0):
            return False
    return True

# This function checks if n is squarefree or not.
def checkSquare(n):
    divisors = listDivisors(n)
    for i in range(1, len(divisors)):
        k = divisors[i]*divisors[i]
        if(n%k==0):
            return False
    return True

# for loop iterates from 2 through 2000
for i in range(2, 2001):
    if(checkJuicy(i) and checkSquare(i)):
        print(i)

# Part 2:

def checkGood(n):
    divisors = listDivisors(n)
    if(len(divisors)>=4):
        sum = divisors[0]+divisors[1]**2+divisors[2]**3+divisors[3]**4
        if(sum==n):
            return True
    return False
# for loop iterates from 2 through 10135.
for i in range(1, 10136):
    if(checkGood(i)):
        divisors = listDivisors(i)
        print("(" + str(divisors[0])+ ", " + str(divisors[1]) + ", " + str(divisors[2]) + ", " + str(divisors[3]) + ")")
