n = int(input())
count = 0
for i in range(20):
    x = int(input())
    if x == -1:
        break
    if x == n:
        count += 1
print("{0} aparece {1} vezes".format(n,count))