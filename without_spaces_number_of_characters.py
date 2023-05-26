s = input()
v = 0 
for i in range(0, len(s)):
    if (ord(s[i])!= 32):
        v += 1
print(v)