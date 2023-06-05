n = int(input())
m = n * n
rev = 0
while n :
    rev = rev * 10 + n % 10
    n //= 10
r_s = rev * rev
p = 0
while r_s :
    p = p * 10 + r_s % 10
    r_s //= 10
if m == p :
    print(True)
else:
    print(False)