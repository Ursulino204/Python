# Declaração de variáveis numéricas como inteiros


H = 3
J = 9 % 2 + H
 
if J < 5:
    K=3
    L =4

elif J < 10:
    K = 6
    L = 7
    H = 8
else:
    K = 9
    L = 10

M = H + K + L * (J - 3)

print(H, J, K, L, M)