# exemplos de fatiamento de strings

nome = 'Guilherme'

# fatiamento
print(nome[0:4]) # pega os caracteres do índice 0 até o 4 (exclusivo)
print(nome[1:4]) # pega os caracteres do índice 1 até o 4 (exclusivo)
print(nome[0:]) # pega todos os caracteres a partir do índice 0
print(nome[:4]) # pega os caracteres do índice 0 até o 4 (exclusivo)
print(nome[::2]) # pega todos os caracteres, pulando de 2 em 2
print(nome[::-1]) # inverte a string

# exemplos de fatiamento de strings com passo
nome = 'Guilherme'

print(nome[0:4:2]) # pega os caracteres do índice 0 até o 4 (exclusivo), pulando de 2 em 2
print(nome[1:4:2]) # pega os caracteres do índice 1 até o 4 (exclusivo), pulando de 2 em 2
print(nome[0::2]) # pega todos os caracteres, pulando de 2 em 2
print(nome[::-1]) # inverte a string

# exemplos de fatiamento de strings com passo negativo
nome = 'Guilherme'

print(nome[0:4:-1]) # pega os caracteres do índice 0 até o 4 (exclusivo), pulando de 1 em 1, mas na ordem inversa
print(nome[1:4:-1]) # pega os caracteres do índice 1 até o 4 (exclusivo), pulando de 1 em 1, mas na ordem inversa
print(nome[0::-1]) # pega todos os caracteres, pulando de 1 em 1, mas na ordem inversa
print(nome[::-1]) # inverte a string

# exemplos de fatiamento de strings com passo negativo
nome = 'Guilherme'

print(nome[0:4:-1]) # pega os caracteres do índice 0 até o 4 (exclusivo), pulando de 1 em 1, mas na ordem inversa
print(nome[1:4:-1]) # pega os caracteres do índice 1 até o 4 (exclusivo), pulando de 1 em 1, mas na ordem inversa
print(nome[0::-1]) # pega todos os caracteres, pulando de 1 em