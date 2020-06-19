import random as rand # Don't forget to import!

numOfCorrect = 0
numOfIncorrect = 0
print("Welcome to the arithmetic quiz!")
print("Enter q at any time to quit.")
print("Round down when doing division:")
finished = False #declaring the "sentinel" variable

while not finished:
    num1 = rand.randint(1, 100) # Randomly generate first number for quiz
    num2 = rand.randint(1, 100)  # Randomly generate second number for quiz 
    operation = rand.randint(0, 3)  # Randomly generate operation
    correctAns = 0  # Set out here so that we don't have to deal scope
    ans = 0 # Set out here so that we don't have to deal scope
    if operation == 0: # if addition
        ans = input(str(num1) + " + " + str(num2) + " = ")
        correctAns = num1 + num2
    elif operation == 1: # if subtraction
        ans = input(str(num1) + " - " + str(num2) + " = ")
        correctAns = num1 - num2
    elif operation == 2: # if multiplication
        ans = input(str(num1) + " * " + str(num2) + " = ")
        correctAns = num1 * num2
    else: # if division
        smallest = min(num1, num2)
        largest = max(num1, num2)
        num1 = largest # set the larger number as the numerator
        num2 = smallest % 11 # set the smaller number as the denominator
        if num2 == 0: # check for 0 in denominator
            num2 = 1
        ans = input(str(num1) + " / " + str(num2) + " = ")
        correctAns = int(num1 / num2)
    if ans == "q" or ans=="Q": # if user wants to quit
        finished = True # don't repeat the while loop
        total = numOfCorrect + numOfIncorrect
        print("Number of Correct:", str(float(numOfCorrect / (total) * 100)) + "%", "(" + str(numOfCorrect) + "/" + str(total) + ")") # calculating the number of correct
        print("Number of Incorrect:", str(float(numOfIncorrect / (total) * 100)) + "%", "(" + str(numOfIncorrect) + "/" + str(total) + ")") # calculating the number of incorrect
    else: # didn't quit (gave an answer)
        ans = int(ans)
        if ans == correctAns:
            print("Correct!")
            numOfCorrect += 1
        else:
            print("Incorrect!")
            numOfIncorrect += 1
print("Bye Bye!")
