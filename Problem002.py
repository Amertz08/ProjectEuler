from ProjectEuler import Fibonacci as F

a = 1
max_value = 1000
values = []
while(F(a) < max_value):
    if(F(a)% 2 == 0):
        values.append(F(a))
    a += 1

print(sum(values))
