# Converter um caractere digitado pelo teclado usando a função input() e retorne esse caractere convertido em Decimal, Hexadecimal e Binário usando a função print.

caractere = char(input("Digite uma letra: "))
decimal = ord(caractere)  
hexadecimal = ord(hex(caractere)) 
binario = ord(bin(caractere))

print('Letra digitada foi:\nSeu valor decimal é: ', decimal,'\nSeu valor hexadecimal é: ', hexadecimal, '\nSeu valor binário é: ', binario)