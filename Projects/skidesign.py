hills = [5, 20, 4, 1, 24, 21]

# This function calculates how much money it will cost-
# given the lowest and highest height a hill can be.
def calculateCost(lowest, highest, hills):
    # total helps us keep track of the cost.
    total = 0
    for i in range(0, len(hills)):
        x = hills[i]
        # if x is lower than the lowest hill allowed, then it costs money to add snow.
        if(x < lowest):
            # we add (lowest-x) feet of snow to the hill, costing us $(lowest-x)*(lowest-x).
            total += (lowest-x)*(lowest-x)
        elif(x > highest):
            # we add (x-highest) feet of snow to the hill.
            total += (x-highest)*(x-highest)
    return total

# main stuff:

# we want to find the the minimum cost.
# we let every value from 1 to 100 be the minimum height and check how much it costs.
# if it costs less than previous values, we keep note.
minimumCost = 2**32-1
for i in range(0, 101):
    cost = calculateCost(i, i+17, hills)
    if(cost < minimumCost):
        minimumCost = cost
        
print(minimumCost)
