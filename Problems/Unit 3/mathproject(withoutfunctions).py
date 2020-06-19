import random as rand

numOfCorrect = 0
numOfIncorrect = 0
print("Welcome to the arithmetic quiz!")
print("Enter q at any time to quit.")
print("Round down when doing division:")
finished = False

while not finished:
    num1 = rand.randint(1, 100)
    num2 = rand.randint(1, 100)
    operation = rand.randint(0, 5)
    correctAns = 0
    ans = 0
    if operation == 0:
        ans = input(str(num1) + " + " + str(num2) + " = ")
        correctAns = num1 + num2
    elif operation == 1:
        ans = input(str(num1) + " - " + str(num2) + " = ")
        correctAns = num1 - num2
    elif operation == 2:
        ans = input(str(num1) + " * " + str(num2) + " = ")
        correctAns = num1 * num2
    else:
        smallest = min(num1, num2)
        largest = max(num1, num2)
        num1 = largest
        num2 = smallest % 11
        if num2 == 0:
            num2 = 1
        ans = input(str(num1) + " / " + str(num2) + " = ")
        correctAns = int(num1 / num2)
    if ans == "q":
        finished = True
        total = numOfCorrect + numOfIncorrect
        print("Number of Correct:", str(float(numOfCorrect / (total) * 100)) + "%", "(" + str(numOfCorrect) + "/" + str(total) + ")")
        print("Number of Incorrect:", str(float(numOfIncorrect / (total) * 100)) + "%", "(" + str(numOfIncorrect) + "/" + str(total) + ")")
    else:
        ans = int(ans)
        if ans == correctAns:
            print("Correct!")
            numOfCorrect += 1
        else:
            print("Incorrect!")
            numOfIncorrect += 1
print("Bye Bye!")
