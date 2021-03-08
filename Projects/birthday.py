import random
# function to generate birthday
def genBirthday():
    numDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num = random.randint(1, 365)
    total = 0
    monthCounter = 1
    date = ""
    while(num > total + numDays[monthCounter]):
        total += numDays[monthCounter]
        monthCounter += 1
    day = num-total
    date = str(monthCounter) + "/" + str(day)
    return date

# function to simulate the birthday paradox
def simulate():
    list = []
    # adding 23 random dates to the list
    for iterator in range(0, 23):
        list.append(genBirthday())
    hasTwoSameBirthday = False
    # nested loop to compare every pair of dates
    for i in range(0, 23):
        for j in range(0, i):
            # if two dates are the same, set hasTwoSameBirthday to true
            if list[i] == list[j]:
                hasTwoSameBirthday = True
    return hasTwoSameBirthday

# function to simulate n times
def simulateN(n):
    trueCounter = 0
    for i in range(0, n):
        if(simulate()):
            trueCounter += 1
    return str(round(100*(float)(trueCounter/n),2)) + "%"

# main
print(simulateN(100000))
