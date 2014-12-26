print('''
This program calculates the sum of the individual digits from 2^n
''')
x = int(input('Enter value: '))
#Calculate value
val = pow(2,x)
#Sum
s = 0

while(round(val/pow(10,len(str(val)) - 1),0)):
    val = round(val%pow(10,len(str(val)) - 1),0)
    s += round(val/pow(10,len(str(val)) - 1),0)
    
print(s)
