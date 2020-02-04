# part 1:

# make these variables large enough
minValue = 10000
minX = 100
minY = 100

for x in range(1, 101):
    for y in range(1, 101):
        value = abs(float((x*x)/(y*y))-float(1/2))
        if(value < minValue):
            minValue = value
            minX = x
            minY = y
print("("+str(minX)+", "+str(minY)+")")

# part 2:
import math

minValue2 = 10000
minA = 100
minB = 100

for a in range(1, 101):
    for b in range(1, 101):
        value2 = abs(float(a-b*math.sqrt(2)-1/3))
        if(value2 < minValue2):
            minValue2 = value2
            minA = a
            minB = b
print("("+str(minA)+", "+str(minB)+")")
