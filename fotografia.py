# OBI 2020 - FASE 2 - PRATIQUE - QUESTÃO FOTOGRAFIA

A,L = map(int, input().split())

N = int(input())

molduras = {}

for i in range(1,N+1):
    X,Y = map(int, input().split())
    molduras[i] = [X,Y]


area_foto = A*L
possiveis = {}
for mold in molduras.items():
    mold_pos = mold[0]
    mold_x = mold[1][0]
    mold_y = mold[1][1]
    area_mold = mold_x * mold_y
    if (area_mold >= area_foto):  # a fotografia seja inteiramente contida dentro na moldura
        if (A <= mold_x and A <= mold_y or L <= mold_x and L <= mold_y): # uma moldura pode ser rotacionada para acomodar a fotografia
            possiveis[mold_pos] = [area_mold]


if (len(possiveis) == 0):
    print(-1)
else:
    chaves = possiveis.keys()
    for c in chaves:
        menor = possiveis[c][0]
        pos = c
        break

    for mold in possiveis.items():
        if (mold[1][0] < menor):
            print(mold)
            menor = mold[1][0]
            pos = mold[0]
    print(pos) # a área da moldura não ocupada pela fotografia seja a menor possível;
