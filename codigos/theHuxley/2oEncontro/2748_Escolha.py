fd, bd, md = map(int,input().split())
fr, br, mr = map(int,input().split())

resposta = 0
if (fr > fd):
  resposta += (fr - fd)

if (br > bd):
  resposta +=  (br - bd)

if (mr > md):
  resposta += (mr - md)

print(resposta)