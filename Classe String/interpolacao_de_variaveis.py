#exemplo 1 - Método % - estilo antigo, as variáveis precisam estar na ordem
nome = 'Guilherme' # %s string
idade = 30  # %d inteiro  %f float, ponto flutuante
profissao = 'Programador'
linguagem = 'Python'

print('ola, me chamo %s, tenho %d anos e trabalho como %s. Minha linguagem preferida é %s' %(nome, idade, profissao, linguagem))  

#exemplo 2 - Método format - similar ao anterior - precisa ser na ordem

nome = 'Guilherme'
idade = 30
profissao = 'Programador'
linguagem = 'Python'

print('Olá, me chamo {}, tenho {} anos e trabalho como {}. Minha linguagem preferida é {}'.format(nome, idade, profissao, linguagem))

#pode mudar a ordem das variáveis
print('Olá, me chamo {0}, tenho {1} anos e trabalho como {2}. Minha linguagem preferida é {3}'.format(nome, idade, profissao, linguagem))

#pode usar nomes para as variáveis
print('Olá, me chamo {nome}, tenho {idade} anos e trabalho como {profissao}. Minha linguagem preferida é {linguagem}'.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))



#exemplo 3 - Método f-string - mais moderno e flexível
nome = 'Guilherme'
idade = 30
profissao = 'Programador'
linguagem = 'Python'

print(f'Olá, me chamo {nome}, tenho {idade} anos e trabalho como {profissao}. Minha linguagem preferida é {linguagem}')

#exemplo 4 - Método f-string - com formatação
nome = 'Guilherme'
idade = 30
altura = 1.80

frase = f'Olá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura:.2f} metros.'

print(frase)  # Saída: Olá, meu nome é Guilherme, tenho 30 anos e minha altura é 1.80 metros

#exemplo 5 - Método f-string - com formatação
nome = 'Guilherme'
idade = 30
altura = 1.80

frase = f'Olá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura:.2f} metros.'

print(frase)  # Saída: Olá, meu nome é Guilherme, tenho 30 anos e minha altura é 1.80 metros

#exemplo 6 - Método f-string - com formatação
nome = 'Guilherme'
idade = 30
altura = 1.80

frase = f'Olá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura:.2f} metros.'

print(frase)  # Saída: Olá, meu nome é Guilherme, tenho 30 anos e minha altura é 1.80 metros


#exemplo 3 - Método f-string -
nome = 'Guilherme'
idade = 30
altura = 1.80

frase = f'Olá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura:.2f} metros.'

print(frase)  # Saída: Olá, meu nome é Guilherme, tenho 30 anos e minha altura é 1.80 metros

