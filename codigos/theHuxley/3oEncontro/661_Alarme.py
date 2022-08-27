entrada = [int(x) for x in input().split(' ')]

while (entrada[0] != 0 or entrada[1] != 0 or entrada[2] != 0 or entrada[3] != 0):
    h1 = entrada[0]
    m1 = entrada[1]
    h2 = entrada[2]
    m2 = entrada[3]
    tempo = ((24 + h2 - h1) * 60 + m2 - m1) % (24 * 60)
    print(tempo)
    entrada = [int(x) for x in input().split(' ')]