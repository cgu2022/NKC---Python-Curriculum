#######################################################################################
# 9.1
# Create a list and print it. The list can be empty or it can contain items. Then use
# the length function len() to print the length of the list.

new_list = [1, 2, 3]
print(new_list)
print("The length of the list is {}".format(len(new_list)))

#######################################################################################
# 9.2
# Using the list created, print out each item by using the [] syntax. ex. list[0] would
# access the first item.

group = ["dog", "cat", "fish", "panda"]

print(group[0])
print(group[1])
print(group[2])
print(group[3])


#######################################################################################
# 9.3
# Use a while loop to print out all the items in the list below.
# You will need to use the len() function and get the list index.
# (Print each element) individually

animals = ["dog", "cat", "fish", "panda"]
i = 0
while i < len(animals):
    print(animals[i])
    i = i + 1

#STOP Here

#######################################################################################
# 9.4A
# Use a for loop to print out all the items in the list below.

nums = [12, 52, -99, 22]

for n in nums:
    print(n)

#######################################################################################
# 9.4B
# Use negative list indexes to print out all of the items in the list from back to
# front. Similar to 9.4A, you will need a for loop.

reverse = [1, 2, 3, 4, 5, 6, 7]


for i in range(-1, -len(reverse)-1, -1):
    print(reverse[i])



#######################################################################################
# 9.5
# Use a for loop to find the smallest number in the list. Print the smallest number.

nums = [55, 5, 11, 0, 44, 9, -12, -33]


smallest = nums[0]
for n in nums:
    if n < smallest:
        smallest = n

print(smallest)


#######################################################################################
# 9.6
# Use a for loop to find the average of all the numbers in the list. Print the average.

nums = [55, 5, 11, 0, 44, 9, -12, -33]


total = 0
for n in nums:
    total += n

print("the average is: {}".format(total/len(nums)))

#Stop Here

#######################################################################################
# 9.7
# Use 2 for loop to loop through this list of lists.

list_of_lists = [[1, 2], [3, 4], [5, 6]]

for l in list_of_lists:
    for num in l:
        print(num)


#######################################################################################
# 9.8
# Create 2 lists of at least size 3. Then add them together into a new list. Print the new list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)


#######################################################################################
# 9.9
# Make another list of 5 elements and change the third element. Print the new list.

test = ['a', 'b', 'c', 'd', 'e']
test[2] = 'k'
print(test)

#######################################################################################
# 9.10
# Make this list have all zeros using a for loop. Print the list.

thing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in thing:
    thing[i] = 0;

#Stop Here

####################################################################################
# 9.11
# Make another list from the first to the sixth elements of test (use slicing)
# Print the list.

test = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

test2 = test[0:5]
print(test2)


#######################################################################################
# 9.12
# Delete the first value in some_list using the "del" keyword. Then remove the first 
# value of the new list using the remove function. Print some_list after the deletions.

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del some_list[0]
some_list.remove(2)
print(some_list)

#######################################################################################
# 9.13
# Use the enumerate function in a for loop to print out the index and item in the for
# loop.
# 0 - "dog"
# 1 - "cat"
# 2 - "mouse"

animal_list = ["dog", "cat", "mouse", "horse", "elephant"]

for i, a in enumerate(animal_list):
    print("{} - {}".format(i, a))

#######################################################################################
# 9.14
# Create a list of at least 5 strings.
# Then ask the user for a string and then print if the string is in the list

lista = ["dog", "cat", "mouse", "horse", "elephant"]
st = str(input())

if st in lista:
        print(True)
else:
        print(False)