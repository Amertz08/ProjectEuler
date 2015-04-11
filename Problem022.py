#   This is not done.

#Take in Names
with open('p022_names.txt') as f:
    for a in f:
        names = a


#   Clean names
names = names.split(',')
clean_names = [name.strip('"') for name in names]
clean_names = sorted(clean_names)

#   Empty score list
scores = [0 for name in clean_names]

#   Each letters associated score
alpha_points = {
'A' :   1,
'B' :   2,
'C' :   3,
'D' :   4,
'E' :   5,
'F' :   6,
'G' :   7,
'H' :   8,
'I' :   9,
'J' :   10,
'K' :   11,
'L' :   12,
'M' :   13,
'N' :   14,
'O' :   15,
'P' :   16,
'Q' :   17,
'R' :   18,
'S' :   19,
'T' :   20,
'U' :   21,
'V' :   22,
'W' :   23,
'X' :   24,
'Y' :   25,
'Z' :   26
}

for a in range(len(clean_names)):
    for b in range(len(clean_names[a])):
        scores[a] += alpha_points[clean_names[a][b]] * (a + 1)

print 'name: %s score: %d' % (clean_names[937], scores[937])
print 'Total sum: %d' % sum(scores)
