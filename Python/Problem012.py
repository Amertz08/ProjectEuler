import time as t
from ProjectEuler import find_factors

'''
Takes in a value as n
calculates nth triangle value
'''
def calcTriangleVal(n):
    s = 0
    while(n > 0):
        s += n
        n -= 1
    return s

#   Start Program
print('''This program finds the value of the first triangle number
 to have over the inputed amount of factors''')
n = int(input('How many factors: '))
factors = []
a = 1

#   Start timer
start = t.time()
#   Run Program
while (len(factors) < n):
    #   Find Triangle value
    x = calcTriangleVal(a)
    #   Find factors of triangle value
    factors = find_factors(x)
    a += 1
#   End Timer
end = t.time()
#   Print results
print('Value: %s Time: %s' % (x, round(end - start, 10)))
