from itertools import product

def recuperar_senha(N,M,K,senha,listas,P):
	posicoes_borradas = [i for i,c in enumerate(senha) if c == "#"]

	combinacoes = list(product(*listas))

	possiveis_senhas = []

	for combinacao in combinacoes:
		senha_lista = list(senha)
		for i,pos in enumerate(posicoes_borradas):
			senha_lista[pos] = combinacao[i]
		possiveis_senhas.append(''.join(senha_lista))

	possiveis_senhas.sort()

	return possiveis_senhas[P-1]

N,M,K = map(int, input().split())

senha = input()
listas = []
for i in range(M):
	S = input()
	listas.append(S)
P = int(input())

senha_recuperada = recuperar_senha(N,M,K,senha,listas,P)
print(senha_recuperada)