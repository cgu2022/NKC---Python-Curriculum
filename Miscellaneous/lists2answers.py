

#######################################################################################
# 1.1
# Use a while loop to print out the numbers 1-10

counter = 1
while counter <= 10:
    print(counter)
    counter += 1

#######################################################################################
# 1.2
# Use a for loop to print out the numbers 1-10

for i in range(1, 11):
    print(i)

#######################################################################################
# 1.3
# Use a for loop to loop through the list below and print out all the numbers. Print
# out the numbers using list indexes (list[index]) instead of by value.

some_list = [2, 4, 6, 8, 10]
for i in range(len(some_list)):
    print(some_list[i])


#######################################################################################
# 1.4
# Use a for loop to add 3 to all the numbers in this list. This means that the list
# should be changed. Then print out all the numbers in the list.

num_list = [3, 4, 5, 9, 10, 11]
for i in range(len(num_list)):
    num_list[i] = num_list[i] + 3
    print(num_list[i])


#######################################################################################
# 1.5
# Use a while loop to add 10 items to an empty list.

empty = []
counter = 0
while counter < 10:
    empty.append(1)
    counter += 1


#######################################################################################
# 1.6
# Use a for loop to loop through this list and find what index the value stored in the
# variable dog exists at. Print the index.

dog = "dog"
some_list = ["cat", "poodle", "mouse", "dog", "human", "elephant", "moose"]
for i in range(len(some_list)):
    if some_list[i] == dog:
        print(i)


#######################################################################################
# 1.7
# Make a for loop which prints the numbers negative 10 to negative 50 inclusive.

for i in range(-10, -51, -1):
    print(i)

#######################################################################################
# 1.8
# Using a for loop, delete the elements in the list below that are at even list indexes.
# Print out the new list after you are done deleting.

some_list = [4, True, "dog", "man", 2.3, False, "nice", "great", 2, 6, 10]

for i in range(len(some_list)-1, -1, -1):
    if i % 2 == 0:
        del some_list[i]

print(some_list)



#######################################################################################
# 1.9
# Move all the values that are greater than 5 into "list2" from "list1". Make sure to
# delete the values you move from "list1".

list1 = [2, 5, 1, 2, 7, 8, 9, 10, 9, 3, 2, 8, 9]
list2 = []

for i in range(len(list1)-1, -1, -1):
    if list1[i] > 5:
        list2.append(list1[i])
        del list1[i]

#######################################################################################
# 1.10
# Similar to the questions before:
# Move all values that are divisible by 2 evenly into "list2"
# Move all values that are divisible by 3 evenly into "list3"
# Move all values that are divisible by 5 evenly into "list5"
# Delete all moved values from list1

list1 = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list2 = []
list3 = []
list5 = []

for i in range(len(list1)-1, -1, -1):
    if list1[i] % 2 == 0:
        list2.append(list1[i])
        del list1[i]
    elif list1[i] % 3 == 0:
        list3.append(list1[i])
        del list1[i]
    elif list1[i] % 5 == 0:
        list5.append(list1[i])
        del list1[i]


#######################################################################################
# 1.11
# Print out all the values in this list.

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j])


#######################################################################################
# 1.12
# Add 1 to all values in a sub list. When you move on to the next sub list, add 2. Then
# for the next sub list add 3.
# If the list is list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# The answer should be: list = [[2, 2, 2], [4, 4, 4], [6, 6, 6]]

list1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

for i in range(len(list1)):
    for j in range(len(list1[i])):
        list1[i][j] = list1[i][j] + i + 1

print(list1)

