flag = True
while flag:
    t, n = map(int, input().split())
    if t == 0 and n == 0:
        flag = False
    else:
        total = 0
        for i in range(t):
            temp = list(input().split())
            total += int(temp[1])
        print(n * 3 - total)