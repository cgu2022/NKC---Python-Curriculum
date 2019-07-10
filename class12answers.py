#######################################################################################
#12.1
# Make a program which has a string variable of your own choosing. Then add code to
# check if is starts with a consonant letter. Hint: make a list of consonats

consanants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
string = "school"

if string[0:1].lower() in consanants:
    print("String starts with consanant") 
else:
    print("String starts with vowel")

#######################################################################################
#12.2
# Make a program which has a string variable of your choosing. Add code to check if it
# starts with a vowel.

vowels = ["a", "e", "i", "o", "u"]
string = "cat"

if string[0:1].lower() in vowels:
    print("String starts with a vowel")
else:
    print("String starts with a consanant")

#######################################################################################
#12.3
# Make a program which takes in a string and converts it to pig latin. Pig latin is a 
# made up language. There are 2 simple rules. 1) If the word starts with a consonant or, 
# consonant group then that letter or group is moved to the end of the word and "ay" is
# added. 2) If the word starts with a vowel you just add "way" to the end.
# explain = explainway
# soup = oupsay

input_string = input("Please enter a word you want to convert to pig latin: ")
vowels = ["a", "e", "i", "o", "u"]
pig_latin = ""

if input_string[0:1].lower() in vowels:
    pig_latin = input_string + "way"
else:
    pig_latin = input_string[1:] + input_string[0:1] + "ay"

print("Changed word: {}".format(pig_latin))


#######################################################################################
#12.4
# Modify the program so that you can make translator for multiple words. Use one of the
# functions you learned about.

input_string = input("Please enter a string you want to convert to pig latin: ")
if input_string.find(".") != -1: # removes period
    input_string = input_string[0:input_string.find(".")]

string_list = input_string.split(" ")
vowels = ["a", "e", "i", "o", "u"]
result = ""
for i, word in enumerate(string_list):
    if word[0:1].lower() in vowels:
        result += word + "way "
    else:
        result += word[1:] + word[0:1] + "ay "
    if i + 1 == len(string_list): # extra
        result = result[0:-1] + "."

print(result)



#######################################################################################
#12.5
# Make a program which takes a string made up of multiple words and transfer each word
# into a list item. Don't use the split function.

string = "this is very cool now really"
some_list = []
current = 0

for i in range(len(string)):
	if string[i] == " ":
		some_list.append(string[current:i])
		current = i + 1
		print(current)

some_list.append(string[current:])
print(some_list)

#######################################################################################
#12.6
# Make your own min/max function (without using min() or max()).
# Write a program that takes a list of numbers, and then returns the min or max of it.

li = [5,6,2,3,4,5,2]
lowest = 2e9
highest = -2e9
for i in li:
    if lowest>i:
        lowest = i
    if highest<i:
        highest = i

print("Lowest: " + str(lowest) + '\nHighest: ' + str(highest))



#######################################################################################
#12.7
# Make your own sort function (without using the sort()).
# Write a program that takes a list of numbers, and then sorts them.

orig = [2,3,5,7,4,5,767,8,6,7,567,55]
st = list()

while len(orig)>0:
    hold = min(orig)
    st.append(hold)
    orig.remove(hold)

print(st)

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

orig = [[2,3],[4,5],[6,7]]
print(orig)
mid = list()

for i in range (0, len(orig)):
    for j in range (0, len(orig[0])):
        mid.append(orig[i][j])
    
inv = list()
for i in range (0, len(orig[0])):
    hold = list()
    for j in range (0, len(orig)):
        hold.append(mid[i*len(orig) + j])
    inv.append(hold)

print(inv)


#######################################################################################
# 12.9 - challenge problem
# Create a encoder program for a string and also make decoder code. Hint: make 2 lists
# using your code

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "."]

# You can change your corresponding code
code = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "^", "*", "/", "%", "#", "@", ")", "(", "[", "]", 
"{", "}", "!", "?", "<", ">", "=", "+", "-"]

string = "cool dog runs well."
encoded_string = ""

for i in range(len(string)):
    if string[i:i+1] in alphabet:
        encoded_string += str(code[alphabet.index(string[i:i+1])])

print("coded string {}".format(encoded_string))

decoded_string = ""


for i in range(len(encoded_string)):
    if encoded_string[i:i+1] in code:
        decoded_string += str(alphabet[code.index(encoded_string[i:i+1])])

print("decoded string {}".format(decoded_string))
