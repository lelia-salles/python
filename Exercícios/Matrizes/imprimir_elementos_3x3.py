# imprimir elementos de uma matriz 3x3 
# nas lihas e colunas correspondentes
# acessar elemento por elemento individualmente

exemplo= [[1,2,3],[4,5,6],[7,8,9]]

print('---------Matriz----------')
print('--------------------------')
for j in range(len(exemplo[0])):  # Itera pelas colunas (0, 1, 2)
    for i in range(len(exemplo)):  # Itera pelas linhas (0, 1, 2)
        print(exemplo[i][j], end='\t')  # Imprime o elemento da coluna atual
    print()  # Pula para a próxima linha após imprimir a coluna
print('--------------------------')