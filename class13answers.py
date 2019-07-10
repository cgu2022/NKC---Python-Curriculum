#######################################################################################
# 13.1
# Make a function which prints out a random string. Then call it.

def p():
    print("HI")

p()

#######################################################################################
# 13.2.a
# Make a function which takes two numbers as parameters and adds them together. Print 
# the sum in the function.

def add(a,b):
    print(a+b)

add(5,5)

#######################################################################################
# 13.2.b
# Make a function which takes two numbers as parameters and adds them together. Return 
# the sum. Then print out the sum.

def add2(a,b):
    return a+b

print(add2(5,5))


#######################################################################################
# 13.3
# Use the addition function you made above and put two of them inside another
# addition function call. ex add(add(2,3), add(3,4))

print(add2(add2(2,3),add2(6,7)))


#######################################################################################
# 13.4
# Make a function that divides 3 numbers (they divide each other). Return none if
# any of them are 0. Then use it

def divide(a,b,c):
    if a==0 or b==0 or c==0:
        return None
    else:
        return a/b/c

print(divide(10,5,2))


#######################################################################################
# 13.5
# Make a function that takes a list and prints each element out seperately. Then use it.

def printlist(li):
    for i in li:
        print(i)

printlist([1,2,3,4,5])


#######################################################################################
# 13.6
# Make your own index function. Return nothing if it can't be found

def ind(a, word):
    for i, x in enumerate(a):
        if x == word:
            return i
    return None

print(ind(["apples","banans","pancakes", "boo"], "boo"))

#######################################################################################
# 13.7
# Fix this code so that it prints:

# 25
# 20

x=20
def print2():
    y=5
    print(x+y)

print2()
print(x)

#######################################################################################
# 13.8
# Fix this code so that it prints:

# 7 5
# 7

x=10 #DON'T CHANGE THIS
def print3():
    x=7
    y=5
    print(x,y)
    return 7

x = print3()
print(x)