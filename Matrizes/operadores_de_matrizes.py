# matriz 2x3 com valores numéricos
# '+' adiciona o conteúdo de uma matriz à outra

num = [[1, 2, 3], [4, 5, 6]]
num + num
num + [[7, 8, 9]]

# matriz 2x2 com valores literais
mat = [['A', 'B'], ['C', 'D']]
mat + mat
mat + [['E', 'F']]

# ´*´ aumenta as linhas das matrizes x vezes. Multiplica a quantidade de listas
# dentro da matriz por um valor numérico desejado.

num = [[1, 2, 3], [4, 5, 6]]
num * 3
teste = [[0]] * 10
teste_2 = [[2, 3]] * 2

# Operador de busca 'in' - procura se um determinado conteúdo pertence a uma lista - retorna True ou False

teste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i = 0
for lin in teste:
    print('O valor 1 pertence a lista', i, 'da matriz')
    print(1 in lin) # vrifica se o valor pertence a lista lin da matriz
    i += 1

# Operador de busca 'not in' - procura se um determinado conteúdo não pertence a uma lista - retorna True ou False
teste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i = 0
for i in teste:
    print('O valor 10 não pertence a lista', i, 'da matriz')
    print(10 not in i) # verifica se o valor não pertence a lista i da matriz
    i += 1

# método len - quantidade de listas de uma matriz e quantidade de colunas de cada linha

teste = [[1, 2], [3, 4], [7, 8, 9]]
# Retorna o número de linha (listas) da matriz teste
print ('Quantidade linhas da matriz teste', i, end=': ')
print(len(teste))
#retorna a qantidade de elementos em cada linha da matriz
i = 0
for lin in teste:
    print('Quantidade elementos da linha', i, end=': ')
    print(len(lin))
    i += 1
print(len(teste[0]))

# método len() de diferentes maneiras para veificar o funcionamento dos operadores aditivo e multiplicativo

# método len()
teste = [[1, 2], [3, 4], [7, 8, 9]]
# retorna o numero de linha nova da mariz teste
print ('Quantidade linhas da matriz teste', i, end=': ')
print(len(teste))

# conacatena a lista na matriz [1,2] teste
teste_2 = [[1, 2]]
# retorna o numero de linhas nova da mariz teste_2
print ('Quantidade linhas da matriz teste_2', i, end=': ')
print(len(teste_2))

#retorna o numero de linha nova da matriz teste_3
#concatena as listas 1 e 2 na matriz teste
teste_3 = [[1, 2]]
print ('Quantidade linhas da matriz teste_3', i, end=': ')
print(len(teste_3))

#duplica a quantidade de listas da matriz
teste_4 = [[1, 2]] * 2
print ('Quantidade linhas da matriz teste_4', i, end=': ')
print(len(teste_4))





# método append() adiciona um elemento ao final da lista
# modifica a lista original sem criar nova lista
# adiciona qualquer tipo de dado e apenas um elemento.
frutas = ["maçã", "banana"]
frutas.append("uva")
print(frutas)  # Saída: ['maçã', 'banana', 'uva']

# método extend() - aduiciona elementos de uma iterável no fim da lista
# adiciona vários elementos

frutas = ["maçã", "banana"]
frutas.extend(["uva", "pêra"])
print(frutas)  # Saída: ['maçã', 'banana', 'uva', 'pêra']

# método intert() - insere um elemento em uma posição específica
frutas = ["maçã", "banana"]
frutas.insert(1, "uva")
print(frutas)  # Saída: ['maçã', 'uva', 'banana']

# método remove() - remove a primeira ocorrência de um elemento específico da lista
frutas = ["maçã", "banana", "uva", "banana"]
frutas.remove("banana")
print(frutas)  # Saída: ['maçã', 'uva', 'banana']

# método pop() - remove o último elemento da lista e o retorna
frutas = ["maçã", "banana", "uva", "banana"]
frutas.pop()
print(frutas)  # Saída: ['maçã', 'banana', 'uva']

# método index() - retorna o índice da primeira ocorrência de um elemento especídico da lista
frutas = ["maçã", "banana", "uva"]
indice_banana = frutas.index("banana")
print(indice_banana)  # Saída: 1

# método count() - retorna a quantidade de vezes que um elemento específico aparece na lista
frutas = ["maçã", "banana", "uva", "banana"]
quantidade_banana = frutas.count("banana")
print(quantidade_banana)  # Saída: 2        

# método sort() - ordena elementos da lista e ordem crescente ou decrescente se reverse = true for especificado
frutas = ["maçã", "banana", "uva"]
frutas.sort()
print(frutas)  # Saída: ['banana', 'maçã', 'uva']

# método reverse() - inverte a ordem dos elementos da lista
frutas = ["maçã", "banana", "uva"]
frutas.reverse()
print(frutas)  # Saída: ['uva', 'banana', 'maçã']

# método clear() remove todos os elementos da lista deixando-a vazia

frutas = ["maçã", "banana", "uva"]
frutas.clear()
print(frutas)  # Saída: []

# método copy() - retorna uma cópia profunda da lista
frutas = ["maçã", "banana", "uva"]
copia_frutas = frutas.copy()
copia_frutas.append("pêra")
print(frutas)  # Saída: ['maçã', 'banana', 'uva']
print(copia_frutas)  # Saída: ['maçã', 'banana', 'uva', 'pêra']


