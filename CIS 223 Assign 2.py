"""
return sum of all even numbers from 0 to 2n
"""

def addEven(n):
    if n == 0:
        return 0
    else:
        lowerbound = 0
        upperbound = 2*n
        return addEvenHelper(lowerbound, upperbound, 0)

def addEvenHelper(lb, ub, evenSum):
    if lb == ub:
        evenSum += ub
        return evenSum
    else:
        evenSum += lb
        return addEvenHelper(lb+2, ub, evenSum)
