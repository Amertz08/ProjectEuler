from ProjectEuler import find_factors, is_prime

print('This program will find the highest prime factor of a number')
value = int(input('Enter a value: '))

#   Get all factors for value
factors = find_factors(value)

#   Iterate over factors highest to lowest
#   Exit if prime
n = 0
while(n < len(factors) and not is_prime(factors[n])):
    n += 1

#   Output results
if(n < len(factors)):  #   n < 0 if no prime factors
    print('Highest prime: %d' % factors[n])
else:
    print('There is no prime factor')
