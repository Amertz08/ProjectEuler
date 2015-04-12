from ProjectEuler import Fibonacci as f
'''
This should work. Might try to use multiprocessing
'''
n = 1
val = f(n)
max_length = 3
while(len(str(val)) < max_length):
    n += 1
    val = f(n)


print('f(%d) = %d' % (n, val))
