#Take in Names
with open('p022_names.txt') as f:
    for a in f:
        val = a

#print(val)
names = []
name = ''
for a in val:
    start = 0

    #Increment count if quote
    if(a == '"'):
        start += 1

    #Add value
    if(start%2 == 0):
        name.append(a)

    #Add name to list
    if(start%2 != 0):
        #print(name)
        #Add name to list
        names.append(name)
        #Reset Name
        name = []

print(names)
#Sort alphabetically
#Calculate alphabetical value
#Calculate name scores
#Sum all scores
