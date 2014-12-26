'''
Takes in a value
returns true if prime
'''
def isPrime(n):
    #Assume that it is prime
    answer = True
    #Get next factor
    a = n - 1
    #Iterate over all possible factors
    while(a > 1):
        #See if value is a factor
        if(n%a == 0):
            answer = False
            #Exit if true
            break
        a -= 1
    return answer

#Start Program
print('''
This program takes in a value and sums all the prime numbers below it
''')

import time

#Take in a value find
n = int(input('Enter a value: '))
#Assign it to end value
a = n

start = time.time()
#Find all the primes
primes = []
while(n > 1):
    #See if prime
    if(isPrime(n)):
        #Add to list
        primes.append(n)
    #Decrement
    n -= 1
end = time.time()
#Print results
print('The sum of the primes below %s is %s' % (a, sum(primes)))
print('Execution time: %s seconds' % round(end - start, 2))
