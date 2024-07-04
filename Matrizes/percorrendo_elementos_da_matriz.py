#percorrendo elementos por meio de for ou while aninhados

matriz = [[0, 0, 0], [0, 0, 0]]

#preenchendo a matriz
print('----------Preenchendo a Matriz----------')
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        matriz[linha][coluna] = int(input(f'Digite um valor para : '))

        #imprime em formato de tabela
        print('----------Matriz----------')
        print('--------------------------')
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                print('|', end='\t')
                print(f'{matriz[linha][coluna]:}', end='\t')
                print()
        print('|')
        print('--------------------------')
        print(linha)