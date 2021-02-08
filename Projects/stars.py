# note: it is also possible to do this iteratively, recursion is not necessary.
def reverseString(str):
    length = len(str)
    # base cases
    if(length == 0 or length == 1):
        return str
    # recursive call
    else:
        # return the last character and call again on the last length-1 characters.
        return str[length-1] + reverseString(str[0:length-1]);

def stars(n):
    for i in range(0, (int)(n/2)):
        str = "";
        for j in range(0, (int)(n/2)):
            if(i%2 == 0 and j >= i):
                str += "*"
            elif(j%2 == 0 and i >= j):
                str += "*"
            else:
                str += " "
        print(str + reverseString(str))

stars(10)
