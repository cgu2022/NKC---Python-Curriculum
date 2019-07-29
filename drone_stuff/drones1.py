# Link to library documentation: http://dev-support.robolink.com/
# Helpful link on python tutorials:
# https://basecamp.robolink.com/cwists/category#products=%5B2%5D&selected_sort_by=alphabetical
# Remember to do all coding on Juypter Notebook!

import CoDrone #to prevent errors

#######################################################################################
# D1.1A
# Make absolute sure you have the following codes in seperate cells:

# Import the library
'''
import CoDrone
from CoDrone import Color, Mode
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


#######################################################################################
# D1.2
# Make the drone go forward for 2 seconds @ 65% powerlevel. Then,
# make it go backwards


#######################################################################################
# D1.3A
# Make the drone eyes blue, and:
# For the drone arm LED, start blue at 10, and then through intervals of 10, get to 250
# Increment the counter every 0.3 seconds. Print the value of blue each time



#####################################################################################
# D1.3B
# Samething as 3A, but while the arm gets bluer, make the green get dimmer.
# So for the eyes, make the eyes green (starting at 250), and through intervals
# of 10, reach 10. 


#######################################################################################
# D1.4A
# Make the drone hover up, land, and then 4 times USING LOOPS
# Display which iteration (count) the program is currently on


#######################################################################################
# D1.4B
# Samething as 3a, but the first time make the drone however for 0.7 seconds,
# 2nd time for 1.4, third time for 2.1, etc. 
# Display how long it will however for each iteration



#######################################################################################
# D1.5
# Ask the user for what direction should the drone go in, for how long, and what power level.
# For example, the user enters 1, 2, and then 70 (three seperate prompts),
# the drone will go forward for 2 seconds @ 70% power level.
# There are six directions: FORWARD, BACKWARD, UP, DOWN, LEFT, and RIGHT


############################################################################################
# D1.6A
# Make the drone fly in a square



############################################################################################
# D1.6A
# Samething as 6A, for each movement command, change the color.
# Ex. First command: Arms are blue
# Second: Arms are green
# etc.




###############################################################################################
# D1.7
# Make the drone fly up for a second at 70% power level. Then, gradually lower the drone down.
# While you lower the drone, display the current height of the drone.
# until it reaches 850mm.


###############################################################################################
# D1.8
# Go explore and have fun!


