# Link to library documentation: http://dev-support.robolink.com/
# Helpful link on python tutorials:
# https://basecamp.robolink.com/cwists/category#products=%5B2%5D&selected_sort_by=alphabetical

import CoDrone #to prevent errors

#######################################################################################
# D1.1A
# Make absolute sure you have the following codes in seperate cells:

# Import the library
'''
import CoDrone
from CoDrone import Color, Mode, Direction
'''

# Imports the library, creates the drone object, pairs the BLE to the drone
'''
import CoDrone
print("Creating drone object")
drone = CoDrone.CoDrone()
print("Getting ready to pair")
drone.pair(drone.Nearest)
print("Paired!")
'''

# ALWAYS NEED THIS IN EVERY PROGRAM:
'''
drone.takeoff()
#Your stuff
drone.move(1.5, 0, 0, 0, 0) #sleep(1.5)
drone.land()
'''

# Emergancy stop:
'''
drone.emergency_stop()
'''

# DO NOT DISCONNECT THE CONTROLLER TO THE COMPUTER OR PRESS THE RESET BUTTON
# WHILE THE PROGRAM IS RUNNING!


#######################################################################################
# D1.1
# Make the drone hover for 4 seconds

i = 4
drone.takeoff()
print("Taking off")
drone.hover(i)
print("Hovering for %i" % i)
drone.land()
print("Landing")

#######################################################################################
# D1.2
# Make the drone go forward for 2 seconds @ 65% powerlevel. Then,
# make it go backwards

drone.takeoff()
drone.go(Direction.FORWARD, 1, 65) 
drone.move(1.5, 0, 0, 0, 0) #sleep(1.5)
drone.land()

#######################################################################################
# D1.3A
# Make the drone eyes blue, and:
# For the drone arm LED, start blue at 10, and then through intervals of 10, get to 250
# Increment the counter every 0.3 seconds. Print the value of blue each time

drone.eye_pattern(Color.Blue, Mode.BLINK, 1)   
i = 10
while i < 250:
    drone.arm_color(50,50,i, 100)
    drone.move(0.3, 0, 0, 0, 0) #sleep(1.5)
    print(i)
    i+=10
drone.arm_off()
print("DONE!")

#####################################################################################
# D1.3B
# Samething as 3A, but while the arm gets bluer, make the green get dimmer.
# So for the eyes, make the eyes green (starting at 250), and through intervals
# of 10, reach 10. 

drone.eye_pattern(Color.Blue, Mode.BLINK, 1)   
i = 10
j = 250
while i < 250:
    drone.arm_color(50,50,i, 100)
    drone.eye_pattern(j, 20, 20, Mode.SOLID)
    drone.move(0.3, 0, 0, 0, 0) #sleep(1.5)
    print(i)
    print(j)
    i+=10
    j-=10
drone.arm_off()
print("DONE!")

#######################################################################################
# D1.4A
# Make the drone hover up, land, and then 4 times USING LOOPS
# Display which iteration (count) the program is currently on

i = 0
while i < 4:
    drone.takeoff()
    print("Taking off")
    drone.hover(2)
    drone.land()
    print("Landing")


#######################################################################################
# D1.4B
# Samething as 3a, but the first time make the drone however for 0.7 seconds,
# 2nd time for 1.4, third time for 2.1, etc. 
# Display how long it will however for each iteration

i = 0
while i < 4:
    drone.takeoff()
    print("Taking off")
    drone.hover(i * 0.7)
    print("Hovering for %i" % (i * 0.7))
    drone.land()
    print("Landing")

#######################################################################################
# D1.5
# Ask the user for what direction should the drone go in, for how long, and what power level.
# For example, the user enters 1, 2, and then 70 (three seperate prompts),
# the drone will go forward for 2 seconds @ 70% power level.
# There are six directions: FORWARD, BACKWARD, UP, DOWN, LEFT, and RIGHT

drone.takeoff()
x = input("Enter choice: ")
y = input("Enter for how long: ")
z = input("Enter power level:")
if int(x) == 1:
    drone.go(Direction.FORWARD, y, z) 
elif int(x) == 2:
    drone.go(Direction.BACKWARD, y, z)
elif int(x) == 3:
    drone.go(Direction.UP, y, z)
elif int(x) == 4:
    drone.go(Direction.DOWN, y, z)
elif int(x) == 5:
    drone.go(Direction.LEFT, y, z)
elif int(x) == 6:
    drone.go(Direction.RIGHT, y, z)
drone.move(1.5, 0, 0, 0, 0) #sleep(1.5)
drone.land()

############################################################################################
# D1.6A
# Make the drone fly in a square

drone.takeoff()
drone.go(Direction.FORWARD, 1, 65) 
drone.move(0.5, 0, 0, 0, 0) #sleep(1.5)
drone.go(Direction.RIGHT, 1, 65) 
drone.move(0.5, 0, 0, 0, 0) #sleep(1.5)
drone.go(Direction.BACKWARD, 1, 65) 
drone.move(0.5, 0, 0, 0, 0) #sleep(1.5)
drone.go(Direction.LEFT, 1, 65) 
drone.move(0.5, 0, 0, 0, 0) #sleep(1.5)
drone.move(1.5, 0, 0, 0, 0)
drone.land()

############################################################################################
# D1.6A
# Samething as 6A, for each movement command, change the color.
# Ex. First command: Arms are blue
# Second: Arms are green
# etc.

z = 1
drone.takeoff()
drone.arm_color(Color.White, 100)
drone.go(Direction.FORWARD, z, 65) 
drone.move(0.5, 0, 0, 0, 0) #sleep(1.5)
drone.arm_color(Color.Azure, 100)
drone.go(Direction.RIGHT, z, 65) 
drone.move(0.5, 0, 0, 0, 0) #sleep(1.5)
drone.arm_color(Color.Yellow, 100)
drone.go(Direction.BACKWARD, z, 65) 
drone.move(0.5, 0, 0, 0, 0) #sleep(1.5)
drone.arm_color(Color.Green, 100)
drone.go(Direction.LEFT, z, 65) 
drone.move(0.5, 0, 0, 0, 0) #sleep(1.5)
drone.move(1.5, 0, 0, 0, 0) #sleep(1.5)
drone.arm_off()
drone.land()


###############################################################################################
# D1.7
# Make the drone fly up for a second at 70% power level. Then, gradually lower the drone down.
# While you lower the drone, display the current height of the drone.
# until it reaches 850mm.

drone.takeoff()
drone.go(Direction.UP, 1, 70)
print("Height: " + str(drone.get_height()/1000))
while(drone.get_height() > 850):
    drone.go(Direction.DOWN, 1, 75)
    print("Height: " + str(drone.get_height()/1000))
print("Height: " + str(drone.get_height()/1000))
drone.move(1.5, 0, 0, 0, 0) #sleep(1.5)
drone.land()

###############################################################################################
# D1.8
# Go explore and have fun!


