# OBI 2021 - NÍVEL 1 - FASE 3 - FESTA OLIMPICA

N = int(input())

conv = [c for c in range(0,N)]

M = int(input())

for i in range(M):
	T = int(input())

	for c in conv[::-1]:
		pos = conv.index(c)
		if (pos >= T and pos % T == 0):
			conv.pop(pos)


conv = sorted(conv)

conv.pop(conv.index(0))


print("-"*10)
if (len(conv) > 10000):
	for i in conv[0:10000]:
		print(i)

else:
	for i in conv:
		print(i)