##################################################################################
# 6.2.1 Create a program using a while loop which asks the user for an integer until that integer is -1. 
# Whenever the integer is not -1, multiply the input by the total.

number = 0
total = 1
while number != -1:
  number = input("Write an integer ")
  total = total * number
  print("The current total is " + str(total))
  

##################################################################################
# 6.2.2 Create a while loop with the condition of True that adds 3 to a total 
# and breaks when the total reaches a multiple of 9.

total = 0
while total < 9:
  total = total + 3
  print("The current total is " + str(total))

##################################################################################
# 6.2.3 Create a program with a nested while loop. 
# The outside while loop should iterate 4 times.
# The inside loop should iterate 10 times.
# The outside loop should use the variable x and the inside loop should use the variable y. 
# Print out the values of x and y for each iteration of the inside

i = 0
j = 0
while i < 4:
  while j < 10:
    print(i)
    print(j)
    j += 1
i += 1
  
##################################################################################
# 6.2.4 Create a program which prints out the following output.
# For this problem we must use two variables, x and y both set to 5. 
#
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

x = 5
while x != 0:
  y = 1
  while y != x + 1:
    print(str(y) , end=' ')
    y += 1
  print("")
  x = x - 1
  
# 6.2.5 Make a while loop that creates this pattern:
#
# *
# * *
# * * *
# * * * *
# * * * * *

x = 1
while x != 6:
  y = 0
  while y != x:
    print("*", end = " ")
    y+=1
  print("\n")
  x+=1

##################################################################################
# Enter 7 temperatures from the keyboard – each on representing a
# daily temperature for the previous week. Sum the 7 values then calculate and print the average
# temperature for the week. 

i = 0
while i != 7:
  temperature = input("Write a new temperature from the week ")
  total = total + temperature
  i+=1
average = total // 7
print("The average temperature of the week is " + average)

###################################################################################
'''
Write a program that asks a user to guess a secret number between 1 and N, where N is a
positive number that the user is prompted for. The program should also prompt the user for
the maximum number of guesses they would like to make. Each time the player makes a guess,
the program shall respond with “correct”, “too low”, or “too high”. The program should keep
track of the number of guesses the user made to discover the secret number. The program
should continue execution until the user has discovered the secret number or has exceeded the
maximum number of guesses. The program shall also allow the user to play the game again
until the user declines.
'''

n = input("What number would you like as the maximum? ")
secretN = random.randint(1, n)
maxGuess = input("How many guesses would you like to be made at most? ")
guesses = 0
count = False
while guesses < maxGuess and count == False: 
  guess = input("What is your guess? ")
  if guess >= secretN:
    print("Too high!")
  elif guess == secretN:
    print("You guessed it!")
    count = True
  else:
    print("Too low!")
  guesses+=1


##################################################################################
# Joe just graduated college and has been offered his first real job as a widget
# designer at Widgets USA, Inc. He is disappointed in the offered beginning salary; 
# only $20,000 per year. But he is promised a 10% raise each year. 
# Other job opportunities offer more to start, but have no promised raises. 
# To help Joe decide, print out a table of his new salary each year until his salary
# reaches or exceeds $50,000. (How many years will it take?) 
# The table is to look as follows. Print your output to a file then turn in the print-out.
#
# Year    Salary
# -------------------
# 1       $ 20,000.00
# 2       $ 22,000.00
# etc...

filename = "SalaryTable.txt"
fileObj = open(filename, "w")
salary = 20000
year = 1
fileObj.write("Year\tSalary\n")
fileObj.write("------------------\n")
while salary <= 50000:
  fileObj.write(str(year) + "\t$ " + format(salary, ",.2f") + "\n")
  year += 1
  salary *= 1.1
fileObj.close()

