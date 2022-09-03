import math

d, vf, vg = map(int, input().split())

while d != -1 and vf != -1 and vg != -1:
    distancia = math.sqrt(pow(12,2) + pow(d,2))
    tf = 12 / vf
    tg = distancia / vg
    
    if tf >= tg:
        print("S")
    else:
        print("N")
    
    d, vf, vg = map(int, input().split())    