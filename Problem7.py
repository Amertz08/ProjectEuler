'''
Takes in a value
returns true if prime
'''
def isPrime(n):
    #Assume that it is prime
    answer = True
    #Not first prime
    if(n < 2): answer = False
    #Find other primes
    else:
        #Get the next factor
        a = n - 1
        #Iterate over all possible factors
        while(a > 1):
            #See if value is factor
            if(n%a == 0):
                #Change answer
                answer = False
                #Exit loop
                break
            #Decrement factors
            a -= 1
    return answer

'''
Program
'''
answer = 'y'
while(answer == 'y'):
    #Prompt desired amount of prime numbers
    num = int(input('Enter the which prime value you would like: '))
    
    #Iterate until desired amount of prime numbers found
    primes = []
    guess = 1
    while(len(primes) < num):
        if(isPrime(guess)):
            primes.append(guess)
        guess += 1

    print(primes[len(primes) - 1])
    answer = input('Do you want to continue? (y/n): ')
