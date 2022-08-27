n = int(input())

while n > 0:
    for i in range(n):
        respostas=list(map(int,input().split()))
        marcadas = [-1 for i in range(5)] 
        for i in range(5):
            if respostas[i] <= 127:
                marcadas[i] = 1
                posicao = i
        pretos = marcadas.count(1)
        if pretos == 1:
            print("ABCDE"[posicao])
        else:
            print("*")
    
    n = int(input())