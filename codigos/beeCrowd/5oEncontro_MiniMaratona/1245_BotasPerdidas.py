
D = [0]*61
E = [0]*61

while True:
    try:
        N = int(input())
        r=0
        #preenche os dois vetores com zeros
        for i in range(61):
            D[i] = 0;
            E[i] = 0;
    
        #enquanto tiver botas (N > 0) faça
        while N:
            N = N - 1
            M, L = input().split()
            M = int(M)
            
            if L=='E':
                E[M] = E[M] + 1
            else:
                D[M] = D[M] + 1
    
            if E[M] and D[M]:
                E[M] = E[M] - 1
                D[M] = D[M] - 1
                r = r + 1
    
        print(r)
    except:
        break
        