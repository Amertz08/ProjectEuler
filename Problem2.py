
#find all the Fibonacci values
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
    
a = 1
values = []
while(F(a) < 4000000):
    if(F(a)% 2 == 0):
        values.append(F(a))
    a += 1
        
print(sum(values))
