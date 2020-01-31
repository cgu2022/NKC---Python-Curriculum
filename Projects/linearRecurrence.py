# part 1:
list = [0, 1, 2, 3, 4]
for i in range(5, 151):
    list.append(list[i-1]+list[i-5])
print(str(list[150]) + "\n")

# part 2:
list2 = [0, 2, 5]
print(2)
print(5)
# counter counts the number of positive numbers printed so far.
counter = 2
n = 1
while(counter < 15):
    list2.append((2-n)*list2[n+1]+(2+n)*list2[n])
    if(list2[n+2]>0 and counter<15):
        print(list2[n+2])
        counter+=1
    n+=1
