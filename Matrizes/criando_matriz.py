"""
matriz é uma lista de listas
"""
# exemplo 1
matriz = [[1, 2, 3], [4, 5, 6]]

print(matriz[0])
print(matriz[0][0])
print(matriz[1][1])


# exemlo 2
matriz_pessoa = [['João', 22, 345768425485],['Maria', 44, 323456789012],['Pedro', 33, 345678901234]]
print(matriz_pessoa)
print(matriz_pessoa[0])
print(matriz_pessoa[1])
print(matriz_pessoa[2])
print(matriz_pessoa[0][0])
print(matriz_pessoa[0][1])
print(matriz_pessoa[0][2])

# modificando um valor em um elemento
matriz_pessoa[0][1] = 25
print(matriz_pessoa)

# Exemplo 3
# criando uma matriz de números
matriz_numeros = [[0,1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

#imprime grupo de elementos da linha 0
print('\nGrupo de números da linha 0: ',matriz_numeros[0])

#imprime grupo de elementos da linha 1
print('\nGrupo de números da linha 1: ',matriz_numeros[1])

#imprime grupo de elementos da linha 2
print('\nGrupo de números da linha 2: ',matriz_numeros[2])

#acessando intervalo de linhas
print('\nGrupo de números da linha 0 e 1: ',matriz_numeros[0:2])

#acessando intervalo de colunas
print('\nGrupo de números da coluna 0 e 1: ',matriz_numeros[0:1,0:2])

#acessando intervalo de linhas e colunas
print('\nGrupo de números da linha 0 e 1 e da coluna 0 e 1: ',matriz_numeros[0:2,0:2]) 

#modificando uma linha
matriz_numeros[0] = [1, 2, 3, 4]
print('\nGrupo de números da linha 0: ',matriz_numeros[0])

#modificando uma coluna
matriz_numeros[:,0] = [1, 2, 3, 4]
print('\nGrupo de números da coluna 0: ',matriz_numeros[:,0])

#modificando uma linha e coluna
matriz_numeros[0,0] = 1
print('\nGrupo de números da linha 0 e coluna 0: ',matriz_numeros[0,0])

