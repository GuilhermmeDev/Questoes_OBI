# QUESTAO toupeira - PROVA TESTE - OBI 2024


def transformaInt(C):
    for n in range(len(C)):
        C[n] = int(C[n])
    return C

def verificaPossibilidade(mapa, sugestao):
    for n in range(len(sugestao[1:])):
        c = 0
        lista = [sugestao[n], sugestao[n+1]]
        status = False
        
        for caminho in mapa.values():
            if (caminho == lista or caminho == lista[::-1]):
                status = True
                c += 1
        
        if (c == 0):
            return 0
            
    return 1
            

dicio = dict()
S,T = map(int, input().split())
id_salao = 1
for c in range(T):
    X,Y = map(int, input().split())
    dicio[id_salao] = [X,Y]
    id_salao += 1
print(dicio)
P = int(input())

possivel = 0
for s in range(P):
    N = input()
    C = N[1:].split()
    N = int(N[0])
    C = transformaInt(C)
    possivel += verificaPossibilidade(dicio, C)
    
print(possivel)
    
    
    