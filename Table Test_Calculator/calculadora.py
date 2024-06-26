def calculadora():
    num1 = float(input('Digite um número:'))
    print(num1)
    num2 = float(input('Digite outro número:'))
    print(num2)
    operacao = input('Digite a operação(+, -, *. /):')
    print(operacao)

    resultado = num1
    # equivale a exempo: resultado = resultado + num2 ou resultado = num 1 + num 2
    if operacao == '+':
        resultado += num2
    elif operacao == '-':
        resultado -= num2
    elif operacao == '*':
        resultado *= num2
    elif operacao == '/=':
        resultado /= num2
    else:
        print('Operação não reconhecida. Tente de novo')
    print('O resultado é: %f' % resultado)

