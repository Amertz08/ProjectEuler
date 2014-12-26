import time as t

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

'''
Takes in a value
returns list of all the factors
'''
def findFactors(n):
    #Create an empty list
    f = []
    #Look at the next lower value
    a = n
    #Iterate through all values
    while(a > 0):
        #Determine if it is a factor
        if(n%a == 0):
            #Add factor to list
            f.append(a)
        a -= 1
    return f

#Start Program
print('''This program finds the value of the first triangle number
 to have over the inputed amount of factors''')
n = int(input('How many factors: '))
factors = []
a = 1

#Start timer
start = t.time()
#Run Program
while (len(factors) < n):
    #Find Triangle value
    x = calcTriangleVal(a)
    #Find factors of triangle value
    factors = findFactors(x)
    a += 1
#End Timer
end = t.time()
#Print results
print('Value: %s Time: %s' % (x, round(end - start, 10)))
