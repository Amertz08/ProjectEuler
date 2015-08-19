'''
Takes in the number of natural numbers wanted
Returns the sum of the squares of those numbers
'''
def sumSquares(n):
    s = 0
    for a in range(1, n + 1):
        s += a*a
    return s
'''
Takes in the number of natural numbers wanted
Returns the square of the sum
'''
def squareSum(n):
    s = 0
    for a in range(1, n + 1):
        s += a
    return s*s

#Get input
n = int(input('Enter the number of natural numbers: '))
#Print results
print('Sum of squares: %s Square of sums: %s Difference %s' % (sumSquares(n), squareSum(n), (squareSum(n) - sumSquares(n))))
