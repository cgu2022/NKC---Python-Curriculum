    #######################################################################################
# 10.1
# Make an empty list and print it

l = []
print(l)

#######################################################################################
# 10.2
# Make a list holding the values 1, 2, 3, 4, 5 and then print the second and fifth item 
# using their index numbers. 

l = [1,2,3,4,5]
print(str(l[1]) + ' ' + str(l[4]))


#######################################################################################
# 10.3
# Use negative list indexes to access the last item in a list of [1, 2, 3, 4] and print
# the item.

l = [1,2,3,4]
print(str(l[-1]))

#######################################################################################
# 10.4
# Create a list and have it store 4 variables of 4 different types. Then print out the 
# list.

l = [True, 1, 5.3, 'Hello']
print(l)


#######################################################################################
# 10.5
# Create a list of lists. The outer list holds 3 inner lists that each hold 2 items. 
# The smaller lists can store anything you want. After you have made the list of lists, 
# print out each small list on a new line.

l = [[1, True], ['Hello', 2.5], [1, 2.4]]
for i in range(len(l)):
    print(l[i])

#######################################################################################
# 10.6
# Take the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and use list slicing to print a list
# that holds [3, 4, 5]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[2:5])

#######################################################################################
# 10.7
# Create a list and use the len() function to print out the length of the list.

l = [1,2,'Hello',True,5.3]
print(len(l))

#######################################################################################
# 10.8
# Create a list. Print it. Then change at least 2 values inside it. Print out the
# changed list.

l = [1,2,3,4,5]
print(l)
l[0] = 2
l[1] = 3
print(l)

#######################################################################################
# 10.9
# Create a list. Use a for loop to loop through the list using a counter variable and
# print each item.

l = [10,20,30,40,50]
for i in range(len(l)):
    print(l[i])

#######################################################################################
# 10.10
# Create a list. Use a for loop to loop through the list using the "in" keyword and 
# print each item.

l = [10,20,30,40,50]
for i in l:
    print(i)

#######################################################################################
# 10.11
# Create a list consisting of integers. Use a for loop to loop through the list and add
# 1 to all the items. Then print out the changed list.

l = [1,2,3,4,5]
for i in range(len(l)):
    l[i] += 1
print(l)

#######################################################################################
# 10.12
# Create 2 lists. Take the lists and create 1 bigger list using both lists. Print the 
# bigger list.

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1 += list2
print(list1)

#######################################################################################
# 10.13
# Create a list of 5 items. Remove 2 items from the end and print each as you remove
# them.

l = [1,2,3,4,5]
print(l[4])
del l[4]
print(l[3])
del l[3]
print(l)


#######################################################################################
# 10.14
# Use the "in" operator to check if a value is in a list. Use an if statement here.

l = [1,2,3,4,5]
if 1 in l:
    print(str(1) + ' is in the list')
else:
    print(str(1) + ' is not in the list')

if 6 in l:
    print(str(6) + ' is in the list')
else:
    print(str(6) + ' is not in the list')

