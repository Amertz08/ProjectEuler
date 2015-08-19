from ProjectEuler import is_palindrome

p = []
#Multiply three digit numbers
for a in range(100, 1000):
    for b in range(a, 1000):
        if(is_palindrome(a*b)):
            #Add value to list if palindrome
            p.append(a*b)

#Print result
print(max(p))
