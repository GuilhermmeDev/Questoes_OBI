# Questão maior valor - PROVA NÍVEL 2 FASE 1 OBI 2022

S = int(input())
A = int(input())
B = int(input())

c = 0
for i in range(A,B+1):
    s = 0
    while i:
        s += i % 10
        i = i // 10
    if (s == S):
        c += 1


print(c);