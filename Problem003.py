'''
Takes in a value
starts at top
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
'''
def findFactors(n):
    #   Create an empty list
    f = []
    #   Exclude 1 and n
    a = 2
    while(a < n):
        #   Add to list if factor
        if n % a == 0:
            f.append(a)
        a += 1
    #   Return factors
    return f

'''
Program
'''
print('This program will find the highest prime factor of a number')
value = int(input('Enter a value: '))

#   Get all factors for value
factors = findFactors(value)
print(factors)
#   Iterate over factors highest to lowest
#   Exit if prime
n = len(factors) - 1
while(not isPrime(factors[n]) and n != 0):
    n -= 1

#   Output results
if(n != 0):  #   n will be 0 if no prime factors
    print('Highest prime: %d' % factors[n])
else:
    print('There is no prime factor')
