# Questão cifra da Nlogônia - PROVA NÍVEL 2 FASE 1 OBI 2021

# Cada consoante deve ser substituída por exatamente três letras
# 1. a própria consoante.

# 2. a vogal mais próxima da consoante original no alfabeto;
# 2.1. se a consoante original está à mesma distância de duas vogais, é escolhida a mais proxima do inicio do alfabeto.

# 3. a consoante que segue a consoante original, na ordem do início ao fim do alfabeto.

# 4. As vogais não são modificadas.


P = str(input())

vogais = ['a','e','i','o','u']
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k', 'l', 'm' ,'n' ,'o', 'p' ,'q', 'r', 's', 't' ,'u', 'v' ,'x' ,'z']

for l in P: # itera sobre cada letra na string
    if (l not in vogais): # testa se é uma consoante
        print(l, end='')  # printa a consoante
        pos_conso = alfabeto.index(l) # posicao do caractere da consoante no array do alfabeto
        for v in alfabeto[pos_conso+1:-1]: # itera o alfabeto da posicao da consoante até o fim do alfabeto
            if (v in vogais): # teste se existe alguma vogal na iteracao
                pos_vogal1 = alfabeto.index(v) # se sim, pega a sua posicao no alfabeto
                break # e para o for loop
        for v in alfabeto[0:pos_conso]: # nesse for, itera sobre o comeco do alfabeto até a consoante
            if (v in vogais): # verifica a vogal na iteracao
                pos_vogal2 = alfabeto.index(v) # pega sua posicao
                # nao pode usar o break, pois é necessario extrair o ultimo aparecimento de vogal
        if (abs(pos_conso - pos_vogal1) == abs(pos_conso - pos_vogal2)): # verifica se a distancia entre a consoante e as duas vogais encontradas são iguais
            print(alfabeto[pos_vogal2],end='') # se for igual, printa a vogal mais próxima do inicio do alfabeto
        else:
            print(alfabeto[pos_vogal1],end='') # se não, as distâncias são diferentes, então pega-se a mais próxima
        for c in alfabeto[pos_conso+1:-1]:  # itera sobre os caracteres nas posicoes seguintes a consoante da string
            if (c not in vogais):  # verifica se é uma consoante
                print(c, end='')  # se sim, é printada
                break # e para o loop
    if (l in vogais): # se não, é uma vogal, logo não é modificada
        print(l,end='') # é impressa na tela


