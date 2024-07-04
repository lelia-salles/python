#criando matriz
matriz = [[0,1,2], [11,12,13]]

#imprimindo linhas da matriz
print('Linas da Matriz')
for lin in matriz:
    print(lin)

#imprimindo elementos da matriz
print('Elementos da Matriz')
print('-----------------------------------------------------')
for lin in matriz:
    for elem in lin:
        print('|', end='\t')
        print(elem, end='\t')
    print('|')
    print('-----------------------------------------------------')