from ProjectEuler import is_prime

'''
Program
'''
answer = 'y'
while(answer == 'y'):
    #Prompt desired amount of prime numbers
    num = int(input('Enter the which prime value you would like: '))

    #Iterate until desired amount of prime numbers found
    primes = []
    guess = 2
    while(len(primes) < num):
        if(is_prime(guess)):
            primes.append(guess)
        guess += 1

    print(primes[len(primes) - 1])
    answer = input('Do you want to continue? (y/n): ')
