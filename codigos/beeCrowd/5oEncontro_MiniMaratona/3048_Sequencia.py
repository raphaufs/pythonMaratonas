
n = int(input())
a = 0
s = 0
for i in range(n):
    v = int(input())
    if (v != a):
        a = v
        s += 1
print(s)