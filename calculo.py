# QUESTAO calculo - FASE 2 - OBI 2023

def somaDigitos(n):
    soma = 0
    while n:
        resto = n % 10
        n = (n - resto)//10
        soma += resto
    return soma
    

S = int(input())
A = int(input())
B = int(input())

c = 0
for n in range(A,B+1):
    if (S == somaDigitos(n)):
        c += 1

print(c)
