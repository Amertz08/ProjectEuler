from ProjectEuler import Fibonacci as F
#   This doesn't work
a = 1
val = F(a)
values = []
while(val <= 4000000):
    if val % 2 == 0:
        values.append(val)
    a += 1
    val = F(a)

assert sum(values) == 4613732, "fail"
print "Pass"
