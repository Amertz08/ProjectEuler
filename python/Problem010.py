from ProjectEuler import is_prime

#   Start Program
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
    if(is_prime(n)):
        #Add to list
        primes.append(n)
    #Decrement
    n -= 1
end = time.time()
#Print results
print('The sum of the primes below %s is %s' % (a, sum(primes)))
print('Execution time: %s seconds' % round(end - start, 2))
