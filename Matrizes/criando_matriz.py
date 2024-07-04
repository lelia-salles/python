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


