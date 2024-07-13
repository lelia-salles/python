import sys

# Listando os argumentos de linha de comando
print("Argumentos de linha de comando:", sys.argv)

# Mostrando o caminho de busca de módulos
print("Caminho de busca de módulos:", sys.path)

# Mostrando o tamanho de um objeto
x = 42
print(f"Tamanho de x ({x}): {sys.getsizeof(x)} bytes")

# Mostrando a plataforma
print("Plataforma:", sys.platform)

# Mostrando a versão do Python
print("Versão do Python:", sys.version)
