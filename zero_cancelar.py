# Questão zero cancelar - PROVA NIVEL 2 FASE 1 OBI 2021
N = int(input())
lista = []
for i in range(N):
    X = int(input())
    lista.append(X)
    if (X == 0):
        lista = lista.pop()
        if (lista == 0):
            lista = list()

print(sum(lista))