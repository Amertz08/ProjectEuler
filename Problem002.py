from ProjectEuler import Fibonacci as F
#   This doesn't work
a = 2
max_value = 10
val = F(a)
values = [val]
while(a < max_value):
    a += 1
    val = F(a)
    values.append(val)



print(values)
