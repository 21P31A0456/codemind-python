n = int(input())
m = list(map(int,input().split()))
s = max(m)
c = 0
for i in m:
    if (len(str(s)) == len(str(i))):
        c += 1
print(c)