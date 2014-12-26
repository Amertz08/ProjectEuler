'''
Takes in a value
returns  n/2 if even
3*n + 1 if odd
'''
def calcVal(n):
    #Even
    if(n%2 == 0): return (n/2)
    #Odd
    else: return(3*n + 1)

'''
Takes in start point
returns count
'''
def calcSeq(val):
    count = 0
    #Iterate until value is 1
    while(val != 1):
        #Calculate value
        val = calcVal(val)
        #Increment count
        count += 1
    return count

#Max value
m = 0
#Count value
c = 1
#End value
x = int(input('Max value: '))
answer = 0
#Iterate until value hits max
while(c <= x):
    #Calculate length of sequence
    n = calcSeq(c)
    #Assign to max if longer
    if(n > m):
        m = n
        answer = c
    c += 1

print('Max: %s Val: %s' % (m, answer))
