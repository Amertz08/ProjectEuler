'''
Takes in a value
high to low
returns True if prime
'''
def isPrime(n):
    #   Start at top
    a = n - 1
    #   Iterate till 1
    while(a > 1):
        #   if a is factor
        if n % a == 0:
            #   Not prime
            return False
        a -= 1
    #   Is prime
    return True

'''
Takes in a value
returns list of all the factors
excluding 1, n, and perfect squares
from highest to lowest
'''
def findFactors(n):
    #   Create an empty list
    f = []
    #   Exclude 1 and n
    a = n - 1
    while(a > 1):
        #   Add to list if factor
        if n % a == 0:
            f.append(a)
        a -= 1
    #   Return factors
    return f

'''
Program
'''
print('This program will find the highest prime factor of a number')
value = int(input('Enter a value: '))

#   Get all factors for value
factors = findFactors(value)
print('factors: %s' % factors)

#   Iterate over factors highest to lowest
#   Exit if prime
n = 0
while(n < len(factors) and not isPrime(factors[n])):
    n += 1

#   Output results
if(n < len(factors)):  #   n < 0 if no prime factors
    print('Highest prime: %d' % factors[n])
else:
    print('There is no prime factor')
