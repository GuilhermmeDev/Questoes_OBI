# Questão trofeu - PROVA NÍVEL 2 FASE 2 OBI 2022

melhores = list()
trofeu = placa = 0
for i in range(5):
    P = int(input())
    if (i == 0):
        melhores.append(P)
        trofeu += 1
    else:
        if (P == melhores[0]):
            trofeu += 1 
        elif (len(melhores) > 1):
            if (P == melhores[1]):
                placa += 1
        else:
            melhores.append(P)
            placa += 1
    print(melhores)

print(trofeu, end=' ')
print(placa)