l = list(map(str, input().split()))
d = []
for i in l:
    c = 0
    for j in i:
        if j in 'AEIOUaeiou':
            c += 1
    d.append(c)
for i in d:
    print(i, end = ' ')