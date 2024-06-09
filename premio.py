P = int(input())
D = int(input())
B = int(input())

pontos_P = P*1 
pontos_D = D*2
pontos_B = B*3

pontos_totais = pontos_B + pontos_D + pontos_P

if (pontos_totais >= 150):
    print('B')
elif (pontos_totais >= 120):
    print('D')
elif (pontos_totais >= 100):
    print('P')
else:
    print('N')