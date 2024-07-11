# Questão Casamento - Pratique - OBI 2021 - Fase 3

def igualaNumeros(A,B):
	if (len(A) > len(B)):
		while len(A) > len(B):
			list_B = list(B)
			list_B.insert(0, '0')
			B = ''.join(list_B)

	elif (len(B) > len(A)):
		while len(B) > len(A):
			list_A = list(A)
			list_A.insert(0,'0')
			A = ''.join(list_A)

	return A,B

def comparaNum(A,B):
	C,D = [],[]
	A = list(A)
	B = list(B)

	A = [int(num) for num in A]
	B = [int(num) for num in B]


	for n in range(len(A)):
		if (A[n] > B[n]):
			C.append(str(A[n]))
			D.append('')
		elif (B[n] > A[n]):
			D.append(str(B[n]))
			C.append('')
		else:
			C.append(str(A[n]))
			D.append(str(B[n]))

	C = ''.join(C)
	D = ''.join(D)

	if (len(C) == 0):
		C = -1
	elif (len(D) == 0):
		D = -1


	return D,C


A = input()
B = input()

result = igualaNumeros(A,B)
A = result[0]
B = result[1]

D,C = comparaNum(A,B)
print(int(D),int(C))