from ProjectEuler import fib
#   This doesn't work
values = []
for x in fib():
    if x > 4000000:
        break
    else:
        if x % 2:
            values.append(x)

assert sum(values) == 4613732, "fail"
print "Pass"
