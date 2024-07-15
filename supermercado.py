# SUPERMERCADO - OBI 2019 - FASE 2 - PRATIQUE 

N = int(input())
lista = []

for mercado in range(N): 
	P,G = map(float, input().split())

	G = int(G)

	valor1kg = (P*1000)/G
	lista.append(valor1kg)

min_lista = min(lista)

print("{:.2f}".format(min_lista))