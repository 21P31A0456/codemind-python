s = input()
v = 'aeiouAEIOU'
lst = []
for i in s:
    if i in v and i not in lst:
        lst.append(i)
print(*lst)