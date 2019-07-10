#######################################################################################
# 7.1
# Write a for loop to count through the numbers 0-10 and print them.

for i in range(0, 11):
    print(i)

#######################################################################################
# 7.2
# Write a for loop to count through the numbers 4-23 and print them.

for i in range(4, 24):
    print(i)

#######################################################################################
# 7.3
# Write a for loop to count through the numbers 0-10 by 2s and print them.

for i in range(0, 11, 2):
    print(i)

#######################################################################################
# 7.4
# Write a for loop to count through the numbers 0-100 by 3s and print them.

for i in range(0, 101, 3):
    print(i)

#######################################################################################
# 7.5
# Write a for loop to count down through the numbers 10-0 and print them.

for i in range(10, -1, -1):
    print(i)

#######################################################################################
# 7.6
# Create a variable holding an integer and convert it to a float. Create a variable
# holding a boolean and convert it to a string. After you have done this, print out
# the converted variables.

int_var = 1
print(float(int_var))
bool_var = True
print(str(bool_var))

#######################################################################################
# 7.7
# Use the format statement to add 2 variables to a print statement. You can create
# these variables in code or have the user input them.

var1 = 2
var2 = 3

print("{} dogs chased {} cars".format(var1, var2))

#######################################################################################
# 7.8
# Use a for loop to create a Fizz Buzz program. A Fizz Buzz counts up from 1 to a
# certain number. If the number is evenly divisible by 3 it outputs "Fizz" instead of
# the number. If the number is evenly divisible by 5 it outputs "Buzz". If it is evenly
# divisible by 3 and 5 then it outputs "FizzBuzz". Finally, if it is not any of those
# cases, it outputs the number.
# ex. 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

for i in range(0, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 