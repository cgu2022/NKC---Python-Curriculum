#######################################################################################
# 5.1
# Make an infinite loop. (But DON'T RUN IT)


while True:
    print("infinite")


#STOP HERE

#######################################################################################
# 5.2
# Make a while loop which prints out the numbers 0 through 10. Here you will need to
# create a counter variable.

counter = 1
while counter <= 10:
    print(counter)
    counter += 1

#######################################################################################
# 5.3
# Make a while loop which counts up by 2s to 100. Print out the current count each loop.

counter = 0
while counter <= 100:
    print(counter)
    counter += 2


#######################################################################################
# 5.4
# Make a while loop which counts down by 3s while the count is greater than 0. Print out
# the count each loop. Start the countdown at 100.

counter = 100
while counter > 0:
    print(counter)
    counter -= 3


 # STOP HERE

#######################################################################################
# 5.5
# Use the input function to continually ask the user for a number and add that number
# to the total. Each loop you should print out the current total. If the user enters
# -1 the loop stops.

total = 0
inp = int(input())
while not inp == -1:
	print("{} + {} = {}".format(total, inp, total+inp))
	total = total + inp
	inp = int(input())

#######################################################################################
# 5.6
# Make a while loop which has 3 variables and changes each one at a different rate. Stop
# the while loop when a variable gets to 100.

a = 0
b = 0
c = 0

while a < 100 and b < 100 and c < 100:
    print("a: {} b: {} c: {}".format(a, b, c))
    a += 1
    b += 2
    c += 3

 # STOP HERE

#######################################################################################
# 5.7
# Make a while loop within a while loop (Nested While Loop). In the outer while loop count up to 10 from 1
# and in the inner loop count up to 3 from 1. Make sure to always reset the 2nd counter
# for each iteration of the first while loop

counter1 = 1
counter2 = 1
while counter1 <= 10:
    while counter2 <= 3:
        print("counter1: {} counter2: {}".format(counter1, counter2))
        counter2 += 1
    counter2 = 1
    counter1 += 1

#######################################################################################
# 5.8
# Make a while loop with a counter variable. If the counter variable equals 100 break
# out of the loop. Use the break statement for this.


counter = 0
while counter < 1000:
    if counter == 100:
        print("exited")
        break
    print(counter)
    counter += 1


#######################################################################################
# 5.9
# Make a string and use the length function to print out the length of the string

string = "this is a cool string"
length = len(string)
print(length)
