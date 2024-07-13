import sys #importa módulo sys

# Verificando o tamanho de diferentes objetos
print(f"Tamanho de um inteiro pequeno (0): {sys.getsizeof(0)} bytes")
print(f"Tamanho de um float (0.0): {sys.getsizeof(0.0)} bytes") # getsizeof obtém tamanho de vários tipos de objetos
print(f"Tamanho de uma string vazia (''): {sys.getsizeof('')} bytes")
print(f"Tamanho de uma lista vazia ([]): {sys.getsizeof([])} bytes")
print(f"Tamanho de uma tupla vazia ([]): {sys.getsizeof(())} bytes")
print(f"Tamanho de um dicionário vazio ({{}}): {sys.getsizeof({})} bytes")
print(f"Tamanho de um conjunto vazio (set()): {sys.getsizeof(set())} bytes")
print(f"Tamanho de True: {sys.getsizeof(True)} bytes")

