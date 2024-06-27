# Funções de entrada e saída

## função print() - saída
``print(*objects, sep=separator, end=end, file=sys.stdout,
flush=False) onde os parâmetros são:``

 

* objects (necessário): são os objetos que serão impressos; pode ser uma string (sequência de caracteres) ou, ainda, variáveis ou constantes. 
*  sep (opcional): especifica como os objetos impressos serão separados. O padrão é um espaço ‘ ’.
*  end (opcional): especifica o caractere impresso no final. O padrão é ``\n`` (nova linha).
*  file (opcional): arquivo para ser preenchido com determinado
conteúdo.
*  flush (opcional): um valor booleano para especificar se a saída será liberada ``True`` ou armazenada em um buffer ``False``. O valor padrão é False.

A função ``print()`` possui códigos especiais, chamados sequências de ``escape``, que são combinações de caracteres iniciadas com o sinal de barra invertida  `` \ `` e algum outro caractere. Essa sequência representa caracteres ou entradas que não podem ser digitadas diretamente no programa, como o ``Enter``(quebra de linha). A sequência de escape é decodificada no momento da impressão e será interpretada como um ``caractere especial`` — por exemplo, aspas simples ou duplas. Ela também pode ser usada para formatar a impressão,originando uma quebra de linha ou tabulação

| Sequencia | Descrição |
|-----------|-----------|
|\n  | Quebra de linha (line feed ou LF)|
|\t | Tabulação horizontal|
|\v | Tabulação vertical (impressoras)|
|\" | Aspa dupla |
|\' | Aspa simples |
|\\ | Barra invertida |
|\0 | Caractere nulo (usado como terminador de strings)|
|\a | Beep de alerta|

## função input() - entrada

`` permite digitar dados de entrada do usuário``
nome = input('Digite seu nome:')
print(nome)

## Conversão de tipos de dados (casting)
``O valor lido pelo input é sempre um string, por isso há necessidade de converter os tipos de dados para que não haja problemas, pois não é possível somar letras, caso o usuário digitar número. Python irá ler números como caracteres de texto.``

nome = input('Digite seu nome:')
idade = int(input('Digite a sua idade:')) - int converte string para inteiro
print('Olá', nome, 'sua idade é':, str(idade))

## Método format()
``O format() é um método da classe string da linguagem Python que
possibilita editar strings de formas diversas. Desse modo, é possível concatenar strings com o comando "Eu tenho {0} anos".format(idade)``

## Método eval()

``O método eval(expr, gloabls=None, local=None) permite que
strings sejam interpretadas como um trecho de código em Python, retornando 12 Comandos de entrada e saída (utilizando a linguagem Python) um objeto. No contexto das funções de input() e print(), a função eval() permite que uma entrada seja interpretada como um comando em Python. A utilização da função eval() garante que a entrada será interpretada como um trecho de código somente quando o desenvolvedor explicitamente programar isso.``

eval(expr, globals=None, locals=None) 

* expr - string
* globals (opcional) - namespace global, padrão None e precisa ser um dicionário.
* locals (opcional) - namespace local, padrão é None, pode ser qualquer mapeamento,

# Método strftime()

``O método strftime(code) retorna uma struct que representa uma data (com dia, mês, ano, hora, minutos e segundos) em um formato específico. É um método da classe datetime``

strftime(code)

* code (necessário): código especial com a informação desejada. Por exemplo: %Y ano com quatro dígitos, %y ano com dois dígitos, %m mês, %d dia, entre outros.




