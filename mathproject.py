#import random
import random

#this function generates the numbers and operand in the equation
def number_generator():
    #create first number
    firstNumber = random.randint(1,9)
    #create the operator
    operator = random.randint(1,4)
        #change the number to each variable
    if operator == 1:
        operator = '+'
    elif operator == 2:
        operator = '-'
    elif operator == 3:
        operator = '*'
    elif operator == 4:
        operator = '/'
    #create second number
    secondNumber = random.randint(1,9)
    return firstNumber, operator, secondNumber

#this function generates the question
def question_generator(firstNumber, operator, secondNumber):
    #put the strings together to make the question
    #if division make sure the bigger number goes first
    if operator == "/":
        #use the division function to determine which is bigger
        biggerNumber, smallerNumber = division(firstNumber, secondNumber)
        #make the question
        question = str(biggerNumber) + ' ' + str(operator) + ' ' + str(smallerNumber) + " ="
    else:
        question = str(firstNumber) + ' ' + str(operator) + ' ' + str(secondNumber) + " ="
    return question

#this function returns which number is bigger or smaller for division
def division(firstNumber, secondNumber):
    if firstNumber >= secondNumber:
        return firstNumber, secondNumber
    if secondNumber > firstNumber:
        return secondNumber, firstNumber

#this function asks and gets the guessed answer from the user
def input_Answer(question):
    check = True
    #ask for the answer
    inputAnswer = input(question + ' ')
    #check if it is q
    if inputAnswer == 'q':
        check = True
    else:
        try:
            inputAnswer = int(inputAnswer)
        except ValueError:
            check = False
    return inputAnswer, check

#this function generates the correct answer
def correct_Answer(firstNumber, operator, secondNumber):
    #find the right answer based on what the operator is
    if operator == '+':
        correctAnswer = firstNumber + secondNumber
    if operator == '-':
        correctAnswer = firstNumber - secondNumber
    if operator == "*":
        correctAnswer = firstNumber * secondNumber
    if operator == '/':
        #division is different - call division function
        biggerNumber, smallerNumber = division(firstNumber, secondNumber)
        correctAnswer = biggerNumber // smallerNumber
    return correctAnswer

#this function checks the answer if it is correct
def check_Answer(inputAnswer, correctAnswer):
    #if they are the same, they are correct
    if inputAnswer == correctAnswer or inputAnswer == "q":
        correct = True
    else:
        correct = False
    return correct

#main
#welcome the user
print("Welcome to the arithmetic quiz!")
print("Enter q at any time to quit.")
print("Please drop any remainders in division.")
#define input answer just to start the loop
inputAnswer = 0

#use a loop until the answer is not what it needs to be
while inputAnswer != 'q':
    #generate the numbers
    firstNumber, operator, secondNumber = number_generator()
    #create the question
    question = question_generator(firstNumber, operator, secondNumber)
    #ask the user what their answer to the question is AND determine if it is ok - bring in the question
    inputAnswer, check = input_Answer(question)
    #find the correct answer
    correctAnswer = correct_Answer(firstNumber, operator, secondNumber)
    #check their answer - use function because it is used in the loop again
    correct = check_Answer(inputAnswer, correctAnswer)

    #Tell the user if they entered an invalid answer / the answer is wrong
    #loop  to re-ask the question
    while check == False or correct == False:
        if check == False:
            print("Please enter an integer.")
        #elif so if check is false (correct will be also) it wont go into both cases
        elif correct == False:
            print("Incorrect!.")
        #re-ask the same question
        inputAnswer, check = input_Answer(question)
        #check their answer again
        correct = check_Answer(inputAnswer, correctAnswer)
    #say that it is right as long as their answer was not q
    if inputAnswer != 'q':
        print("Correct!")
    #if it is q, loop ends after and says bye
    else:
        print("OK bye!")
