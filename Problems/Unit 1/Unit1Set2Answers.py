#######################################################################################
# 2.1
# change what is stored in the variables to another types of data

some_var = int("23")
some_var2 = float(1)
some_var3 = str(True)
some_var4 = int(1.32)



#######################################################################################
# 2.2
# using the variables a, b, c, and d, print out the number 5
# use a combonation of +, -, *, /
# ex. print(a + b - c * d) -> this is not the answer

a = 10
b = 2
c = 3
d = 12
print(a * b * c / d)


#######################################################################################
# 2.3
# create 2 variables with 1 holding your first name and 1 holding your last name
# add them together with a space so it prints nicely
# ex. print("John" + " " + "Melon") -> "John Melon"


first_name = "John"
last_name = "Melon"

print(first_name + " " + last_name)


#######################################################################################
# 2.4
# Make 2 variables. 1 Variable will be a string and the other will be a number. Then
# add them together and print them out.

num_var = 10
str_var = "This number is cool: "
print(str_var + num_var)

#######################################################################################
# 2.5
# Make 1 variable. Make another variable and set it equal to the other variable. Then
# print out the second variable to see what is stored.

var1 = 10
var2 = "some var"
var2 = var1
print(var2)


#######################################################################################
# 2.6
# Make a math equation with at least a +, -, /, * and (). Store this equation in a
# variable and then print out what is stored in the variable.

equation = 5*(9+2)/2-3
print(equation)


#######################################################################################
# 2.7
# Create string, int, float, and boolean variables. Then print them all out.

name = "John Melon"
cool_number = 4
cool_fraction = 0.75
boolean_var = True

print(name)
print(cool_number)
print(cool_fraction)
print(boolean_var)

#######################################################################################
# 2.8
# Print the two variables together for each pair
# Example:
# a = "Hi "
# b = " People"
# print(a + b) --> Hi People
# Hint: you may need to use casting!

a = "5 "
b = "cats"

print(a + b)

a = 5
b = "dogs"

print(str(a) + b)

a = "Average: "
b = 14.5

print(a + str(b))