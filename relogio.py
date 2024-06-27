# Questão Relogio - OBI 2024 - NÍVEL 2 - Fase 1

H = int(input())
M = int(input())
S = int(input())

T = int(input())

H_T,M_T,S_T = 0,0,0
if (T >= 3600):
    H_T = T//3600
    T -= 3600*H_T
if (T >= 60):
    M_T = T//60
    T -= 60*M_T
if (T < 60):
    S_T = T


R_H = H + H_T
R_M = M + M_T
R_S = S + S_T

if (R_S >= 60):
    R_M += R_S//60
    R_S -= 60*(R_S//60)

if (R_M >= 60):
    R_H += R_M//60
    R_M -= 60*(R_M//60)

if (R_H >= 24):
    dif = 24*(R_H//24)
    R_H = R_H - dif


print(R_H)
print(R_M)
print(R_S)

