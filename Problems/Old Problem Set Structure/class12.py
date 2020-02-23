#######################################################################################
# 12.1
# Make a program which has a string variable of your own choosing. Then add code to
# check if is starts with a consonant letter. Hint: make a list of consonats

#######################################################################################
# 12.2
# Make a program which has a string variable of your choosing. Add code to check if it
# starts with a vowel.


#######################################################################################
# 12.3
# Make a program which takes in a string and converts it to pig latin. Pig latin is a 
# made up language. There are 2 simple rules. 1) If the word starts with a consonant or, 
# consonant group then that letter or group is moved to the end of the word and "ay" is
# added. 2) If the word starts with a vowel you just add "way" to the end.
# explain = explainway
# soup = oupsay


#######################################################################################
# 12.4
# Modify the program so that you can make translator for multiple words. Use one of the
# functions you learned about.

#######################################################################################
# 12.5
# Make a program which takes a string made up of multiple words and transfer each word
# into a list item. Don't use the split function.


#######################################################################################
# 12.6
# Make your own min/max function (without using min() or max()).
# Write a program that takes a list of numbers, and then returns the min or max of it.

#######################################################################################
# 12.7
# Make your own sort function (without using the sort()).
# Write a program that takes a list of numbers, and then sorts them.

#######################################################################################
# 12.8 - challenge problem

# Take a list of lists, and than transpose it to inverted dimensions

# ex. [[2, 3], [4, 5], [6, 7]] --> [[2, 3, 4], [5, 6, 7]]
# (3 by 2 --> 2 by 3)
# ex. [[2, 3, 5, 7], [4, 5, 767, 8], [6, 7, 567, 55]] --> [[2, 3, 5], [7, 4, 5], [767, 8, 6], [7, 567, 55]]
# (3 by 4 --> 4 by 3) 

# use the list() to make an empty list
# ex. num = list() (an empty list)

# Note: it is always guaranteed that every list in that list
# will always have the same length.
# For example, this would not be allowed: [[2,3],[5,6,7,8]] becauase
# the first list has length 2, and the second list has length 4. Both lengths will have to be the same

#######################################################################################
# 12.9 - challenge problem
# Create a encoder program for a string and also make decoder code. Hint: make 2 lists
# using your code

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# You can change your corresponding code
code = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "^", "*", "/", "%", "#", "@", ")", "(", "[", "]", 
"{", "}", "!", "?", "<", ">", "="]
