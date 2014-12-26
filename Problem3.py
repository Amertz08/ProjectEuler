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

'''
Takes in a value
returns list of all the factors
'''
def findFactors(n):
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
Program
'''
print('This program will find the highest prime factor of a number')
value = int(input('Enter a value: '))

#Get all factors for value
factors = findFactors(value)

#Iterate over factors highest to lowest
#Exit if prime
n = 0
while(not isPrime(factors[n])):
    if(isPrime(factors[n])):
        break
    n += 1

#Output results
print('Highest prime: %s' % factors[n])
    
