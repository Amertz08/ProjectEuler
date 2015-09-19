'''
fibonacci generator
'''
def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b


'''
n       :   int
return  :   boolean
Takes in a value n
returns True if prime
'''
def is_prime(n):
    #   Get next factor
    a = n - 1
    #   Iterate over all possible factors
    while(a > 1):
        #   See if value is a factor
        if(n%a == 0): return False
        a -= 1
    return True

'''
n       :   int
return  :   list
Takes in a value n
returns list of all the factors from high to low
'''
def find_factors(n):
    #Create an empty list
    f = []
    #Look at the next lower value
    a = n - 1
    #Iterate through all values
    while(a > 1):
        #Determine if it is a factor
        if(n%a == 0):
            #Add factor to list
            f.append(a)
        a -= 1
    return f

'''
x       :   int
return  :   boolean
takes in an int x
returns True if value is a boolean
'''
def is_palindrome(x):
    value = str(x)
    a = 0
    b = len(value) - 1
    while(a != b and (b >= 0 or a < len(value))):
        if(value[a] != value[b]): return False
        a += 1
        b -= 1
    return True
