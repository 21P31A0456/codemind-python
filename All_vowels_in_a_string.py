s = input()
v = 'aeiou'
lst = []
for i in s:
    if i in v and i not in lst:
        lst.append(i)
if len(v) == len(lst):
    print(True)
else:
    print(False)