# OBI 2021 - NÍVEL 1 - FASE 3 - PLANO DE ESTACIONAMENTO

N = int(input())

M = int(input())

estac = dict()   # dict do estacionamento

for vaga in range(N,0,-1):
	estac[vaga] = 0  # é igual a zero, pois não está ocupada

print(estac)

c = 0

for i in range(M):
	V = int(input())
	for vaga,estado in estac.items():
		if (vaga <= V):
			if (estado == 0):
				print(vaga, estado)
				estac[vaga] = 1
				c += 1
				break

print(c)
