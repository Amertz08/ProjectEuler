values = []

for x in range(1, 1001):
    if(x%3 == 0):
        values.append(x)
    elif(x%5 == 0):
        values.append(x)

print(sum(values))
