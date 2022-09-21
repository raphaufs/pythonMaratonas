import math

while True:
    try:
        d, vf, vg = map(int, input().split())
        distancia = math.sqrt(pow(12,2) + pow(d,2))
        tf = 12 / vf
        tg = distancia / vg
        
        if tf >= tg:
            print("S")
        else:
            print("N")
    except:
        break