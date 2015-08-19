with open("../p013.txt") as f:
    content = f.readlines()

answer = 0
for num in content:
    answer += int(num)

assert int(str(answer)[:10]) == 5537376230, "fail"
print "pass"
