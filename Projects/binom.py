def binomSum(n):
    total = 0
    for k in range(0, n+1):
        total += binom(n, k)
    return total

def binom(n, k):
    numerator = 1
    denominator = 1
    for i in range(n-k+1, n+1):
        numerator *= i
    for j in range(1, k+1):
        denominator *= j
    return numerator/denominator

print(binomSum(10))
