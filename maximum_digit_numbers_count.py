n = int(input())
m = list(map(int,input().split()))
b = []
for i in m:
    i = str(i)
    b += [len(i)]
for  i in m:
    i = str(i)
    if (len(i) == max(b)):
        print(i, end = ' ')