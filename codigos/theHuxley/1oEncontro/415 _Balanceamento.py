n = int(input())

while n > 0:
    s = input()
    parenteses = 0
    colchete = 0
    for caractere in s:
        if caractere == "(":
            parenteses += 1
        elif caractere == ")":
            parenteses -= 1
        if caractere == "[":
            colchete += 1
        elif caractere == "]":
            colchete -= 1
        if parenteses < 0 or colchete < 0:
            break;
    if parenteses == 0 and colchete == 0:
        print("Yes")
    else:
        print("No")
    n -= 1

