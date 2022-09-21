
teste = 0
n = int(input())
while (n > 0):
    x = -10000
    v = -10000
    y =  10000
    u =  10000
    for i in range(n):
        x1, y1, u1, v1 = map(int,input().split())
        if x1 > x:
            x = x1
        if y1 < y:
            y = y1
        if u1 < u:
            u = u1
        if v1 > v:
            v = v1
    teste +=  1
    print("Teste {0}".format(teste))
    if (x < u) and (v < y): 
        print("{0} {1} {2} {3}".format(x,y,u,v))
    else:
        print("nenhum")
    print("")
    n = int(input())