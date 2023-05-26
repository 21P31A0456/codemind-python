s = input()
v = 'aeiou'
lst = []
for i in v:
    if i not in s and i not in lst:
        lst.append(i)
if len(lst) == 0:
    print(0)
else:
    print(*lst)