def factorial(n):
    if(n == 1):
        return 1
    else:
        return n * factorial(n - 1)

'''
takes in a value
returns sum of individual digits
'''
def sumVal(n):
    s = 0
    for x in str(n):
        s += int(x)
    return s

#Start program
print('''Program takes in a value, finds factorial,
 calculates sum of the digits in factorial''')
a = int(input('Enter a value: '))
b = factorial(a)

print('input: %s factorial: %s sum: %s' % (a, b, sumVal(b)))
