# QUESTAO contas - PROVA TESTE - OBI 2024

V = int(input())
A = int(input())
F = int(input())
P = int(input())

contas = [A,F,P]
c = 0
for conta in contas:
    if (V >= conta):
        V -= conta
        c += 1 

print(c)


