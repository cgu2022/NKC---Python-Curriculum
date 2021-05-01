def addPolynomials(poly1, poly2):
    polySum = [0] * (max(len(poly1),len(poly2)))
    i = 0
    # while i is still less than the length of one of the polynomials
    while(i < max(len(poly1),len(poly2))):
        # checking if we have not reached the end of one of the polynomials
        if(i < len(poly1)):
            polySum[i] = polySum[i] + poly1[i];
        if(i < len(poly2)):
            polySum[i] = polySum[i] + poly2[i];
    return polySum
def multiplyPolynoials(poly1, poly2):
    polyProd = [0] * (len(poly1)*len(poly2))
    # outer loop
    for i in range(0, len(poly1)):
        # inner loop
        for j in range(0, len(poly2)):
            # the product of the two terms is the coefficient of x^{i+j}
            polyProd[i+j] = polyProd[i+j] + poly1[i]*poly2[j]
    return polyProd
def printPolynomial(poly1):
    returnString = ""
    notFirstTerm = False
    for i in range(0, len(poly1)):
        if(poly1[i] != 0):
            if(notFirstTerm):
                returnString += "+"
            if(i == 0):
                returnString += str(poly1[i])
                notFirstTerm = True
            elif(i == 1):
                if(poly1[i] != 1):
                    returnString += str(poly1[i]) + "x"
                else:
                    returnString += "x"
            else:
                if(poly1[i] != 1):
                    returnString += str(poly1[i]) + "x^" + str(i)
                else:
                    returnString += "x^" + str(i)
    print(returnString)
# main
poly1 = [1,1,1]
poly2 = [1,1]
printPolynomial(multiplyPolynoials(poly1,poly2))
printPolynomial(multiplyPolynoials(poly2,multiplyPolynoials(poly2, multiplyPolynoials(poly2, poly2))))
