def FatorI(index : list):
    FI = 1 # Fator de Influência
    possb = []
    for j in index:
        c = 0  # contador maior que o FI
        for i in index:
            if (FI <= i):
                c += 1
                if (c > FI):
                    break
        if (FI <= c):
            possb.append(FI)
        FI += 1
        
    return max(possb)

N = int(input())

index = []
for i in range(N):
    R = int(input())
    index.append(R)
print(FatorI(index))
