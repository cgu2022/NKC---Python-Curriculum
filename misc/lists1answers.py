
#######################################################################################
# 1.1
# Make a program which finds the largest value in this list

li = [2, 3, 51, 2, 44, 56, 72, 2, 3, 5, 6]
largest = 0
for i in li:
    if i < largest:
        largest = i
print(largest)


#######################################################################################
# 1.2
# Write a program which multiplies all the values in this list and then prints the 
# product.

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = 1
for i in li:
    product *= i
print(product)

#######################################################################################
# 1.3
# Write a program which reverses the order of the list. This time use 2 lists. Print
# out the reversed list.

li = [1, 2, 3, 4, 5, 6]
new_list = []
for i in range(-1, -len(li)-1):
    new_list.append(li[i])
print(new_list)

#######################################################################################
# 1.4
# Write a program which reverses the order of the list. Don't make another list. Print
# out the reversed list.

li = [1, 2, 3, 4, 5, 6]
temp = li[0]
counter = -1
for i in range(int(len(li)/2)):
    li[i] = li[counter]
    li[counter] = temp
    temp = li[i+1]
    counter -= 1
print(li)

#######################################################################################
# 1.5
# Write a program which prints out the number of strings in the list with a length less
# than 3.

li = ["hi", "dog", "ca", "nj", "house"]
for i in li:
    if len(i) < 3:
        print(i)


#######################################################################################
# 1.6
# Delete all duplicate values from this list. Use the "del" keyword and for loop(s)

some_list = [1, 2, 1, 3, 3, 5, 7, 8, 9, 1, 4, 5, 6, 8, 9, 10, 2, 3, 4, 6, 8, 9]

for i, v in enumerate(some_list):
    for j, v1 in enumerate(some_list):
        if i != j and v == v1:
            del some_list[j]
print(some_list)

# Another solution using list range function:
i = len(some_list) - 1
while i > 0:
	for j in range(i-1, -1, -1):
		if some_list[i] == some_list[j]:
			del some_list[j]
			i -= 1
	i -= 1

print(some_list)

#######################################################################################
# 1.7
# Sort this list into increasing order.

increasing = [9, 1, 2, 8, 10, 5, 4, 3, 6, 7]

for i in range(len(increasing)):
    for j in range(i, len(increasing)):
        if increasing[i] > increasing[j]:
            temp = increasing[i]
            increasing[i] = increasing[j]
            increasing[j] = temp
print(increasing)


#######################################################################################
# 1.8
# Sort this list into decreasing order.

decreasing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in range(len(decreasing)):
    for j in range(i, len(decreasing)):
        if decreasing[i] < decreasing[j]:
            temp = decreasing[i]
            decreasing[i] = decreasing[j]
            decreasing[j] = temp
print(decreasing)




#######################################################################################
# 1.9
# Loop through the following list and print the pairs of numbers when multiplied
# together give a product which can be evenly divided by 2. For example, a number pair
# which would work would be 2 and 6 since they equal 12 when multiplied together.

multiples = [2, 5, 7, 1, 0, 8, 6, 9, 10, 3, 11]


for i in range(len(multiples)):
    for j in range(i, len(multiples)):
        if (multiples[i] * multiples[j]) % 2 == 0:
            print("{} x {} % 2 = 0".format(multiples[i], multiples[j]))








