matriz_quadrada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diag_princ = [0,0,0]
diag_sec = [0,0,0]

for i in range(len(matriz_quadrada)):
    for j in range(len(matriz_quadrada)):
        if i == j:
            diag_princ[i] = matriz_quadrada[i][j]
        if i + j == len(matriz_quadrada) - 1:
            diag_sec[i] = matriz_quadrada[i][j]

print(diag_princ)
print(diag_sec)