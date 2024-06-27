# Tipos de dados
Definem características e comportamentos de um valor para o interpretador que ocupam memória. Por exemplo, operações matemáticas podem consumir 24 bytes.

## Tipos existentes chamados de built-in:

|Texto|str(string)|
|-----|-----------|
|numérico|int,fçoat,complex|
|sequência|list,tuple,range|
|Mapa|dict|
|Coleção|set,frozenset|
|Booleano|bool|
|Binário|bytes, bytearray, memoryview|

# Built-in
`` Os built-ins em Python são funções, tipos, exceções e outros objetos que estão disponíveis por padrão em qualquer programa Python, sem a necessidade de importá-los de módulos externos. Eles fazem parte da biblioteca padrão do Python e são muito úteis para realizar uma variedade de operações comuns. Vou descrever alguns dos principais built-ins em Python``

## Exemplos:
### Funções Built-in
São funções que podem ser chamadas diretamente, sem necessidade de importação. Aqui estão algumas das mais usadas:

* print(): Imprime a saída para o console.
* len(): Retorna o comprimento (número de itens) de um objeto.
type(): Retorna o tipo de um objeto.
* int(), float(), str(): Convertem valores para inteiros, ponto flutuante e string, respectivamente.
 input(): Lê uma entrada do usuário.
 sum(): Retorna a soma de um iterável.
* min(), max(): Retornam o valor mínimo e máximo de um iterável.
* range(): Gera uma sequência de números.
list(), dict(), set(), tuple(): Funções para criar listas, dicionários, conjuntos e tuplas.
### Tipos Built-in
Python oferece vários tipos de dados integrados:

* int: Números inteiros.
* float: Números de ponto flutuante.
* str: Cadeias de caracteres (strings).
* list: Listas, que são coleções ordenadas e mutáveis.
tuple: Tuplas, que são coleções ordenadas e imutáveis.
* dict: Dicionários, que são coleções de pares chave-valor.
* set: Conjuntos, que são coleções não ordenadas de elementos únicos.
* bool: Valores booleanos (True e False).

### Exceções Built-in
São classes de exceções que podem ser usadas para tratar erros:

* Exception: Classe base para todas as exceções.
* ValueError: Levantada quando uma função recebe um argumento com o tipo correto, mas com valor inapropriado.
* TypeError: Levantada quando uma operação ou função é aplicada a um objeto de tipo inapropriado.
* IndexError: Levantada quando se tenta acessar um índice inexistente em uma sequência.
KeyError: Levantada quando se tenta acessar uma chave inexistente em um dicionário.

### Outras Funções e Objetos Úteis

* open(): Abre um arquivo e retorna um objeto de arquivo.
* sorted(): Retorna uma lista ordenada dos elementos de um iterável.
* enumerate(): Retorna um objeto enumerador.
* zip(): Retorna um iterador de tuplas, onde a i-ésima tupla contém o i-ésimo elemento de cada um dos iteráveis fornecidos.

## Memória
`` O consumo de memória de cada objeto em Python pode variar com base em diversos fatores, incluindo a implementação específica do Python (por exemplo, CPython, PyPy), a versão do Python, e o sistema operacional subjacente.``
### Tipos de Implentação
#### CPython

CPython é a implementação de referência da linguagem de programação Python

* Implementação Original: CPython é a implementação original do Python e é escrita em C. Quando as pessoas se referem a "Python", geralmente estão falando sobre CPython.
* Interprete e Compilador: CPython compila o código-fonte Python em bytecode, que é então interpretado pela máquina virtual CPython.
* Extensibilidade: CPython permite a escrita de módulos em C, que podem ser carregados dinamicamente e usados dentro de programas Python. Isso é útil para criar extensões de alto desempenho.
* Bibliotecas e Suporte: CPython tem o maior número de bibliotecas e a comunidade mais ampla, tornando-o a escolha padrão para a maioria dos projetos.

#### PyPy

PyPy é uma implementação alternativa da linguagem Python, focada em velocidade e eficiência.

* Just-In-Time (JIT) Compilation: PyPy usa compilação just-in-time, o que significa que ele compila código Python em tempo de execução, resultando em uma execução geralmente mais rápida do que CPython.

*  Compatibilidade: PyPy é compatível com CPython, o que significa que a maioria dos programas que funcionam em CPython também funcionarão em PyPy sem modificação.
*  Memória: PyPy também tem melhorias de gerenciamento de memória em relação ao CPython, o que pode resultar em menor uso de memória para alguns programas.
*  Menor Latência: Programas que requerem menor latência podem se beneficiar da execução mais rápida do PyPy.Just-In-Time (JIT) * 
* Compilation: PyPy usa compilação just-in-time, o que significa que ele compila código Python em tempo de execução, resultando em uma execução geralmente mais rápida do que CPython.
*  Compatibilidade: PyPy é compatível com CPython, o que significa que a maioria dos programas que funcionam em CPython também funcionarão em PyPy sem modificação.
* Memória: PyPy também tem melhorias de gerenciamento de memória em relação ao CPython, o que pode resultar em menor uso de memória para alguns programas.
* Menor Latência: Programas que requerem menor latência podem se beneficiar da execução mais rápida do PyPy.Just-In-Time (JIT) * * * Compilation: PyPy usa compilação just-in-time, o que significa que ele compila código Python em tempo de execução, resultando em uma execução geralmente mais rápida do que CPython.

#### Módulo sys
O módulo sys em Python fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador. 

* sys.argv: Lista dos argumentos de linha de comando passados para o script Python.
* sys.path: Lista dos diretórios que o interpretador procura por módulos ao importar.
* sys.modules: Dicionário de todos os módulos atualmente importados.
* sys.exit(): Função para sair do programa Python.
sys.getsizeof(): Retorna o tamanho de um objeto em bytes.
* sys.platform: Retorna uma string que identifica a plataforma onde o Python está sendo executado (por exemplo, "win32", "linux").
* sys.version: Retorna uma string que contém informações sobre a versão do Python em uso.






|  Tipos  | Memória    |
|---------|------------|
|  Inteiros ``int``       | O tamanho básico de um objeto inteiro é de cerca de 24 bytes para pequenos inteiros (em CPython). O tamanho pode aumentar para inteiros maiores.           |
|  Ponto Flutuante ``float``      | O tamanho básico de um objeto float é de 24 bytes em CPython           |
|  Strings ``str``       |   O tamanho básico de um objeto string é de 49 bytes, mais 1 byte por caractere (em CPython). Strings maiores podem ocupar mais memória.         |
| Listas ``list``        | Uma lista vazia ocupa cerca de 64 bytes. Cada item adicional na lista ocupa espaço adicional (geralmente, 8 bytes por referência ao objeto, mais o tamanho do próprio objeto).           |
|  Tuplas ``tuple``       | Uma tupla vazia ocupa cerca de 48 bytes. Cada item adicional ocupa cerca de 8 bytes por referência ao objeto, mais o tamanho do próprio objeto.           |
|  Dicionários ``dict``       |   Um dicionário vazio ocupa cerca de 240 bytes. Cada par chave-valor adicional consome espaço adicional (geralmente, 8 bytes por referência ao objeto, mais o tamanho do próprio objeto).
         |
|   Conjuntos ``set``      |  Um conjunto vazio ocupa cerca de 224 bytes. Cada item adicional consome espaço adicional (semelhante ao de um dicionário).          |
| Booleanos ``bool`` | Objetos booleanos (True e False) são singletons e compartilham a mesma instância. Cada um ocupa o mesmo espaço de um objeto inteiro (24 bytes). |

<black>comando ``python`` no terminal do VSCode abre um terminal interativo, não há necessidade digitar print para alguns testes para prompt do computador digitar `` python nomeDoArquivo.py `` para executar no console <black>