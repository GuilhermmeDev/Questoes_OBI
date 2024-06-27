# Questão Concurso - OBI 2024 - NÍVEL 2 - Fase 1

def transformaInt(A):
    for n in range(len(A)):
        A[n] = int(A[n])

    return A

N,K = map(int, input().split())
A = input().split()
A = transformaInt(A)
C = 0
if (len(A) == N):
    if (K == 1):
        print(max(A))
    else:

        for i in range(len(A)):
            c = 0
            maior = A[i]

            
            for nota in A:
                if (nota >= maior):
                        c += 1

            if (c >= K and maior > C):
                C = maior
                
        print(C)
        
        
