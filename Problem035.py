from ProjectEuler import is_prime
max_val = 10000

#   All prime values from 2 to max_val inclusive
primes = [x for x in range(2,max_val + 1) if is_prime(x)]
print 'Found primes'
def is_circular_prime(val):
    c = 0
    for a in range(len(str(val))):
        y = str(val % (1 * 10**(len(str(val)) - 1)))
        x = str(val / (1 * 10**(len(str(val)) - 1)))
        val = int(y + x)
        if(is_prime(val)): c += 1

    if c < len(str(val)):   return False
    else:   return True

circle_primes = [prime for prime in primes if is_circular_prime(prime)]
print len(circle_primes)
print circle_primes
