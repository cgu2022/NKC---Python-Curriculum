# Link to library documentation: http://dev-support.robolink.com/
# Helpful link on python tutorials: https://basecamp.robolink.com/cwists/category#products=%5B2%5D&selected_sort_by=alphabetical

#######################################################################################
# D1.1
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
# D1.2
# Make the drone hover for 4 seconds




#######################################################################################
# 3.3
# make inequalities which all evaluate to True using <=, >=, ==, !=


#######################################################################################
# 3.4
# make inequalities which all evaluate to False using <=, >=, ==, !=

#######################################################################################
# 3.5
# use and, or, not to combine inequalities using ()
# 1 evaluates to True using "and", 1 evaluates to False using "and"
# 1 evaluates to True using "or", 1 evaluates to False using "or"
# 1 evaluates to True using "not", 1 evaluates to False using "not"
# try to use a variety of >=, ==, !=, <=, <, >
