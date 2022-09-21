
cont = 0
jogadores, partidas = map(int, input().split())

gols = [0]*jogadores

for i in range(jogadores):
    gols[i] = list(map(int, input().split()))
    
    
for i in range(jogadores):
    naoFezGol = False
    for j in range(partidas):
        if gols[i][j] == 0:
            naoFezGol = True
    if naoFezGol == False:
        cont = cont + 1

print(cont)