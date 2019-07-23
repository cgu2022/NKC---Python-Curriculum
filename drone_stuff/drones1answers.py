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

# Land the drone code
'''
drone.land()
'''

# Emergancy stop:
'''
drone.emergency_stop()
'''

# DO NOT DISCONNECT THE CONTROLLER TO THE COMPUTER OR PRESS THE RESET BUTTON
# WHILE THE PROGRAM IS RUNNING!

#######################################################################################
# D1.1B
# If the drone is upside down, flash some lights and print something to tell us

if drone.is_upside_down():
    drone.arm_strobe()
    print("UPSIDE DOWN!")
else:
    drone.arm_off()

#######################################################################################
# D1.2
# Make the drone hover for 4 seconds

i = 4
drone.takeoff()
print("Taking off")
drone.hover(i)
print("Hovering for %i" % i)
drone.land()
print("Landing")


#######################################################################################
# D1.3A
# Make the drone hover up, land, and then 6 times 

for i in range(1, 7):
    drone.takeoff()
    print("Taking off")
    drone.hover(2)
    drone.land()
    print("Landing")


#######################################################################################
# D1.3B
# Samething as 3a, but the first time make the drone however for 0.7 seconds,
# 2nd time for 1.4, third time for 2.1, etc.

for i in range(1, 7):
    drone.takeoff()
    print("Taking off")
    drone.hover(i)
    print("Hovering for %i" % i)
    drone.land()
    print("Landing")

