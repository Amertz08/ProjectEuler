'''
Takes in a value, start point, and end point
returns true if  value is evenly divisible from start to end
'''
def eDiv(value, start, end):
    #Assume it is evenly div through range
    answer = True
    for a in range(start, end + 1):
        if (value % a != 0):
            answer = False
            break
    return answer

#Prompt input
print('''
Program will find smallest number than can be evenly divisible
by all valuse in range 1 to whatever value entered by user
''')
end = int(input('Enter last value of range: '))

#Find value
n = 1
while(not eDiv(n, 1, end)):
    n += 1

#Print answer
print(n)
