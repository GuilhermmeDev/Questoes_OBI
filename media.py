# Questão Média ou Mediana da OBI Pratique Nível 2, Fase 2 

A,B = map(int, input().split())

C = 0

while True:
	lista = sorted([A,B,C]) # ordem crescente

	mediana = lista[1] # pega o meio da lista

	media = (A + B + C)/3 # faz a media

	if (media != mediana):
		C += 1
	else:
		print(C)
		break