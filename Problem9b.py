from time import time as t

'''
Takes in min and max of values
returns guess
'''
def guess(minVal, maxVal):
    return round((maxVal - minVal)/2,0)

'''
Takes in value for A
returns max value for be
'''
def maxB(aVal):
    return round((999 - (aVal + 1))/2,0)

'''
Takes in a, b, c
returns -1 if a^2 + b^2 < c^2
0 if a^2 + b^2 = c^2
1 if a^2 + b^2 > c^2
'''
def pythSquare(x, y, z):
    if(x*x + y*y < z*z): return -1
    elif(x*x + y*y == z*z): return 0
    else: return 1

#Initial Guess
aMin = 1
aMax = 332
a = guess(aMin, aMax)
bMax = maxB(a)
b = guess(a, bMax)
b += a
c = 1000 - (a + b)

while(pythSquare(a,b,c) != 0):
    #Left side too low
    if(pythSquare(a,b,c) == -1):
        a = guess(aMin, aMax)
        bMax = maxB(a)
        b = guess(a, bMax)
        b += a
        c = 1000 - (a + b)
    
        
print('A; %s B: %s C: %s' % (a, b, c))
print(pythSquare(a,b,c))
