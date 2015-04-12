from ProjectEuler import Fibonacci as f
'''
This should work. Might try to use multiprocessing
'''
n = 1
val = 1
max_length = 6
while(len(str(val)) < max_length):
    val = f(n)
    n += 1

print('f(%d) = %d' % (n, val))
