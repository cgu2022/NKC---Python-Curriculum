
#######################################################################################
# 14.1
# Make a function that takes 3 integer parameters and prints the sum off all 3 numbers

a = 1
b = 2
c = 3

def sum_3(a, b, c):
    print(a+b+c)

sum_3(a, b, c)

#######################################################################################
# 14.2
# Make a function which adds two numbers together and returns the sum. Then call that 
# function and use the same function as parameters. For example: add(add(1, 2), add(3, 5))

def add(a, b):
    return a + b

print(add(add(1, 2), add(3, 5)))

#######################################################################################
# 14.3
# Make your pig latin program into a function which takes in a single string as a
# parameter and returns the converted string. Print the returned string.

def pig_latin(string):
    vowels = ["a", "e", "i", "o", "u"]
    if string[0:1] in vowels:
        return string + "way"
    else:
        return string[1:] + string[0] + "ay"

#######################################################################################
# 14.4
# Make a function which takes in a list of integers as a parameter. Then return the
# number of even integers in the list.

list1 = [22, 32, 55, 90, 24, 67]

def count_evens(l):
    count = 0
    for i in range(len(l)):
        if l[i] % 2 == 0:
            count += 1
    return count


#######################################################################################
# 14.5
# Make a function which takes in a list of integers as one parameter and an integer as
# another parameter. Then remove all duplicates of the integer in the list if any
# duplicates exist. Return the new list and print it.

list1 = [1, 1, 2, 3, 4, 2, 4, 3, 5, 5, 6, 7, 8, 9]

def remove_dupes(l, val):
    for i in range(len(l)-1, -1, -1):
        if l[i] == val:
            del l[i]
    return l

print(remove_duplicates(list1, 2))

#######################################################################################
# 14.6
# Make a multiplication function which takes in two numbers as parameters. Call the 
# function once you made it. Then put in add() functions as the number parameters. Print
# the returned result.

def mult(a, b):
    return a * b

print(mult(add(2, 2), add(3, 3)))

#######################################################################################
# 14.7
# Make a function which takes a list of ints as a parameter and returns the largest
# number.

def largest(l):
    largest = l[0]
    for i in range(len(l)):
        if l[i] > largest:
            largest = l[i]
    return largest


#######################################################################################
# 14.8
# Make a function which takes a list of ints as a parameter and returns the smallest
# number.

def smallest(l):
    smallest = l[0]
    for i in range(len(l)):
        if l[i] < smallest:
            smallest = l[i]
    return smallest

#######################################################################################
# 14.9
# Make a function which combines the functions from 14.7 and 14.8 to find the difference
# between the smallest and largest values in an int list. Return the difference.

def diff_small_large(l):
    return largest(l) - smallest(l)


#######################################################################################
# 14.10
# Make a function which takes in an int as a parameter and returns the number the int
# starts with. For example: 54->5, 10->1, 20->2, 34->3, 101->1

def get_first(num):
    while num >= 10:
        num /= 10
    return int(num)

#######################################################################################
# 14.11
# Use the function above to create a function which takes in a list of ints and only
# sums together numbers that don't start with 1, 4, 7. Return the sum.

list1 = [1, 22, 34, 25, 90, 28, 42, 54, 30, 98, 55]

def something(l):
    total = 0
    for i in range(len(l)):
        if get_first(l[i]) != 1 or get_first(l[i]) != 4 or get_first(l[i]) != 7:
            total += l[i]

    return total


#######################################################################################
# 14.12
# Make a function which takes in an int and returns the number of numbers in the int.
# Ex: 2->1, 55->2, 65->2, 5->1, 100->3, 776->3, 1000->4

def num_nums(num):
    prev = 1
    counter = 0
    while num >= prev:
        prev *= 10
        counter += 1
    return counter


#######################################################################################
# 14.13
# Make a function which calculates the answer to a number raised to another number.
# One parameter is the base and another is the exponent. Ex: 2^2->4, 2^3->8, 5->2->25

def power(a, b):
    total = 1
    for i in range(b):
        total *= a
    return total

#######################################################################################
# 14.14
# Make a function which takes an int as a parameter and returns the last number.
# Hint: Use functions from 14.10 and 14.12 and 14.13
# Ex: 45->5, 20->0, 566->6

def last_num(num):
    while num >= 10:
        num = (num % (first_num(num) * power(10, num_nums(num)-1)))
    return num
