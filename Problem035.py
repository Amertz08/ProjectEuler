from ProjectEuler import is_prime

'''
val     :   int
return  :   boolean
Takes in a val and returns True if
the val is a circular prime
'''
def is_circular_prime(val):
    c = 0
    d = len(str(val))
    for a in range(d):
        y = str(val % (1 * 10**(d - 1)))
        x = str(val / (1 * 10**(d - 1)))
        val = int(y + x)
        if(is_prime(val)): c += 1

    if c < d:   return False
    else:   return True

max_val = 10000

#   All prime values from 2 to max_val inclusive
primes = [x for x in range(2,max_val + 1) if is_prime(x)]
print 'Found primes'

'''
Should rewrite to remove circular primes already found
'''
circle_primes = [prime for prime in primes if is_circular_prime(prime)]
print len(circle_primes)
print circle_primes
