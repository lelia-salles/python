# imprimir elementos de uma matriz 3x3 
# nas lihas e colunas correspondentes
# acessar elemento por elemento individualmente

exemplo= [[1,2,3],[4,5,6],[7,8,9]
]

for i in range(len(exemplo)):
    for j in range(len(exemplo[i])):
        print(exemplo[0][0])
        print(exemplo[0][1])
        print(exemplo[0][2])

        print()

print('---------Matriz----------')
print('--------------------------')
for i in range(len(exemplo)):
        for col in range(len(exemplo[i])):
                print( end='\t')
                print(f'{exemplo[i][col]:}', end='\t')
                print()
        #print('|')
        #print('--------------------------')
        #print(i)