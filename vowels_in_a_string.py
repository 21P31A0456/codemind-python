s = input()
v = input()
n = 0
for i in range(0, len(s)):
    if s[i] == v:
        n = 1
        print("True")
        print(i)
        break
if n == 0:
    print("False")