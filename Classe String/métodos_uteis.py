#Masúscula, minúscula e título
curso = 'PYthon'
# tudo maiúsiculo
print(curso.upper()) 
# tudo minúsculo
print(curso.lower())
# primeira letra maiúscula
print(curso.title())

#Eliminando espaços em branco

curso_1 = '   Python     '
#elimina espaços da esquerda e direita
print(curso_1.strip())
#elimina espaços da direita
print(curso_1.rstrip())
#elimina espaços da equerda
print(curso_1.lstrip())  

#Centralização
curso_2 = 'Python'
#centraliza o texto
print(curso_2.center(10))
#centraliza o texto com espaços
print(curso_2.center(10,'#'))

#join (mais usado pra listas sem necessidade de fazer um for)
curso_3 = 'Python'

print('#'.join(curso_3))

#split
curso_4 = 'Python'
print(curso_4.split())

#replace
curso_5 = 'Python'
print(curso_5.replace('Python','Java'))

#count
curso_6 = 'Python'
print(curso_6.count('Python'))

#find
curso_7 = 'Python'
print(curso_7.find('Python'))

#index
curso_8 = 'Python'
print(curso_8.index('Python'))


