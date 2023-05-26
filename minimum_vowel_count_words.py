s = list(map(str,input().split()))
lst = []
v = 'aeiouAEIOU'
for i in s:
    c = 0
    for j in i:
        if j in v:
            c += 1
    lst.append(c)
lst1 = []
for i in lst:
    if  i == min(lst):
        lst1.append(i)
print(len(lst1))