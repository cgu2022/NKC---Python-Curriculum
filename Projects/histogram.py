list = [4,1,1,3,2,4,1,0,9,9,9,7,6]
freqList = [0,0,0,0,0,0,0,0,0,0]
for i in range(0, len(list)):
    x = list[i]
    freqList[x] += 1
for j in range(0, len(freqList)):
    s = ""
    for k in range(0, freqList[j]):
        s += "*"
    print(str(j) + "|" + s)
