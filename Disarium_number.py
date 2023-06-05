n = int(input())
l = len(str(n))
temp = n
i = 0
s = 0
while temp > 0 :
    i = temp % 10
    s = s + int(i ** l)
    temp = temp // 10
    l = l - 1
if s == n:
    print(True)
else :
    print(False)