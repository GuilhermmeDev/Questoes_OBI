def transformaInt(caixas : list):
    for i in range(len(caixas)):
        caixas[i] = int(caixas[i])
    return caixas

N = int(input())
caixas = input().split()
if (len(caixas) == N):
    caixas = transformaInt(caixas)
    caixas = sorted(caixas)

subindo = True
contra_peso = 0
subiu = []
while subindo:
    if (len(caixas) > 0):
        for i in caixas:
            if (i - contra_peso <= 8):
                subiu.append(i)
                if (max(caixas) == i):
                    caixas.pop(caixas.index(i))
                    contra_peso = 0
                else:
                    contra_peso = i
                    subiu.pop(subiu.index(i))
            else:
                subindo = False
                print('N')
                break
    else:
        subindo = False
        print('S')
