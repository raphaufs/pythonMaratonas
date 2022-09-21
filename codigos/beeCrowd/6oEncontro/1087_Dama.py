
def igual(x1 , y1, x2, y2):
    return (x1 == x2 and y1 == y2)

def mesma_linha(x1, y1, x2, y2):
    return (x1 == x2 or y1 == y2)

def mesma_diagonal(x1, y1, x2, y2):
	return (x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2)


x1, y1, x2, y2 = map(int, input().split())

while x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
    
    if igual(x1 , y1, x2, y2):
        print(0)
    elif mesma_linha(x1 , y1, x2, y2) or mesma_diagonal(x1, y1, x2, y2):
        print(1)
    else: 
        print(2)
    
    x1, y1, x2, y2 = map(int, input().split())