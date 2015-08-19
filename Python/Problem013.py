with open("../p013.txt") as f:
    content = f.readlines()

answer = sum([int(num) for num in content])

assert int(str(answer)[:10]) == 5537376230, "fail"
print "pass"
