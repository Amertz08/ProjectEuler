def isPalindrome(x):
    value = str(x)
    #Assume they are palindromes
    answer = True
    a = 0
    b = len(value) - 1
    while(a != b and (b >= 0 or a < len(value))):
        if(value[a] != value[b]):
            answer = False
            break
        a += 1
        b -= 1
    return answer

p = []
#Multiply three digit numbers
for a in range(100, 1000):
    for b in range(a, 1000):
        if(isPalindrome(a*b)):
            #Add value to list if palindrome
            p.append(a*b)

#Print result
print(max(p))
