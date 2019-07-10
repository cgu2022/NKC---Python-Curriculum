#######################################################################################
# 11.1
# Create a list of 10 items. Use the index function to find at least 1 of the items
# and print the index.

list1 = [0,1,2,3,4,5,6,7,8,9]
print(list1.index(1))

#######################################################################################
# 11.2
# Make an empty list. Use append to add 2 items to the list. Then print out the list.

list1 = []
list1.append(0)
print(list1)

#######################################################################################
# 11.3
# Make an empty list. Use append and a for loop to add 10 items to the list. Then print
# out the list.

list1 = []
for i in range(10):
    list1.append(i)
print(list1)

#######################################################################################
# 11.4
# Create a list of 10 items. Then use the remove function to delete one of the items.
# Print the new list.

list1 = [0,1,2,3,4,5,6,7,8,9]
list1.remove(0)
print(list1)


#######################################################################################
# 11.5
# Create a list of strings. Then call the sort function on it. Then print the new
# sorted list.

list1 = ['DEF', 'JkL', 'GhI', 'ABC']
list1.sort()
print(list1)

#######################################################################################
# 11.6
# Create a list of numbers in random order. Call the sort function on the list and
# print the sorted list.

list1 = [22,32,1,2,3,54,323,4,4,234]
list1.sort()
print(list1)

#######################################################################################
# 11.7
# Create a list of 10 numbers in random order. Call the sort function on the list with 
# the reverse parameter set to true. Print the sorted list.

list1 = [22,32,1,2,3,54,323,4,4,234]
list1.sort(reverse=True)
print(list1)

#######################################################################################
# 11.8
# Create a string. Use slicing notation like in a list to get part of the string. Print
# out the partial string.

s = 'NJCSSA'
print(s[0:2])

#######################################################################################
# 11.9
# Create a string. Use the split function to make a list of each character from the
# string. Print out the list.

s = "njcssa.org"
print(list(s))

#######################################################################################
# 11.10
# Make a program which splits a string like in the previous example using string
# slicing. Add characters to a list and print out the list.

s = 'abcdef'
list1 = []
for i in range(len(s)):
    list1.append(s[i:i+1])
list1.append('g')
list1.append('h')
print(list1)

#######################################################################################
# 11.11
# Create a string and use the slice function to get a slice of the string. Print out
# the slice.

s = 'abcdef'
t = slice(3)
print(s[t])

#######################################################################################
# 11.12
# Create a string and use any of string functions you learned from the slideshow not
# already used to modify the string. Print the modified string.

#Sample Answer
s = 'NJCSSA'
print(s)
l = list(s)
print(l)
l.append('.org')
print(l)
print(s[0:2])
print(s[slice(2,6)])

