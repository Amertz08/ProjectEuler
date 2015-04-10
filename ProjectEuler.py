'''
n       :   int
finds the n-th term fibonacci number
'''
def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci(n-1)+Fibonacci(n-2)


'''
n       :   int
return  :   boolean
Takes in a value n
returns True if prime
'''
def is_prime(n):
    #   Assume that it is prime
    answer = True
    #   Get next factor
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

'''
n       :   int
return  :   list
Takes in a value n
returns list of all the factors
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
