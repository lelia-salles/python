#exemplo 1
frase = "Olá, meu nome é %s, tenho %d anos e minha altura é %.2f metros." % (nome, idade, altura)

print(frase)  # Saída: Olá, meu nome é João, tenho 30 anos e minha altura é 1.80 metros.

#exemplo 2
nome = 'Guilherme'
idade = 30
altura = 1.80

frase = f'Olá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura:.2f} metros.'

print(frase)  # Saída: Olá, meu nome é Guilherme, tenho 30 anos e minha altura é 1.80 metros

#exemplo 3
nome = 'Guilherme' # %s string
idade = 30  # %d inteiro  %f float, ponto flutuante
profissao = 'Programador'
linguagem = 'Python'

print('ola, me chamo %s, tenho %d anos e trabalho como %s. Minha linguagem preferida é %s')  # Saída: Olá, meu nome é Guilherme, tenho'