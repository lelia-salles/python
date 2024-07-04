"""
/workspaces/python-basico/Matrizes/matriz_bidimensional.py

Uma matriz bidimensional, também conhecida como matriz, é uma estrutura de dados que organiza elementos em linhas e colunas. 
Imagine uma tabela com linhas e colunas, cada célula da tabela armazena um valor.

"""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

"""
nome_matriz[i][j]

i = linha
j = coluna

"""
# Acessando o elemento na primeira linha e primeira coluna (valor 1)
elemento = matriz[0][0]
print(f"Elemento na posição [0][0]: {elemento}")

# Acessando o elemento na segunda linha e terceira coluna (valor 6)
elemento = matriz[1][2]
print(f"Elemento na posição [1][2]: {elemento}")

"""
Matrizes são formadas por diagonais principais e secundárias.
A diagonal principal é obtida pela igualdade entre i e j.
A diagonal secundária é obtida pela igualdade entre i e len(matriz) - j - 1 ou (i + j = len(matriz) - 1)
maatriz representa uma lista de listas. Uma matriz quadrada 3x3.
len(matriz) retorna o número de linhas da matriz.
len(matriz[0]) retorna o número de colunas da matriz.
range(len(matriz)) retorna um objeto iterável que contém os índices das linhas da matriz. 
    Uma sequência de números começando em 0, e indo até (mas não incluindo) o tamanho da matriz.
range(len(matriz[0])) retorna um objeto iterável que contém os índices das colunas da matriz.
"""

# Diagonal principal
print("Diagonal principal:")
for i in range(len(matriz)):
    print(matriz[i][i])

# Diagonal secundária
print("Diagonal secundária:")
for i in range(len(matriz)):
    print(matriz[i][len(matriz) - i - 1])