'''
Not a huge fan of exhuastive method
Think some sort of binary search
'''
import time
start = time.time()

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        for c in range(b + 1, 1000):
            if((a*a + b*b) == c*c) and ((a + b + c) == 1000):
                values = [a, b, c]
                break

end = time.time()
print('''a: %s b: %s c: %s
a + b + c = %s
a^2 + b^2 = c^2 %s''' % (values[0], values[1], values[2],
                         values[0] + values[1] + values[2],
                         values[0]*values[0] + values[1]*values[1] == values[2]*values[2]))
print('Execution time: %s' % round((end - start),2))
