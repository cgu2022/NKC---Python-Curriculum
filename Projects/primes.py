# This function sums all the proper divisors of n.
def sumDivisors(n):
    total=0
    for i in range(1,n):
        if(n%i)==0:
            total+=i
    return total

# This function tests whether n is amicable or not.
def isAmicable(n):
    sum=sumDivisors(n)
    if(sum!=n):
        if(sumDivisors(sum)==n):
            return True
    return False

# This function tests whether n is prime or not.
def isPrime(n):
    if(n==1):
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
    return True

# This function tests whether n is perfect or not.
def isPerfect(n):
    sum=sumDivisors(n)
    if(sum==n):
        return True
    return False

# for loop
for i in range(1, 421):
    if(isAmicable(i)):
        print(str(i) + " is amicable")
    elif(isPrime(i)):
        print(str(i) + " is prime")
    elif(isPerfect(i)):
        print(str(i) + " is perfect")
