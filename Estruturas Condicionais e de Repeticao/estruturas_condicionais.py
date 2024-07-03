# if - compõe um único desvio, testa a lógica e se for verdadeiro, o blocoserá executado
saldo = 2000.0
saque = float(input("informe valo do saque"))

if saldo >= saque:
    print("saque realizado com sucesso")
if saldo < saque:
    print("saldo insuficiente")

# if/else - compõe dois desvios, se o bloco de lógica go verdadeiro o if é executado se não for, o else é executado
if saldo >= saque:
    print("saque realizado com sucesso")
else:
    print("saldo insuficiente")

# if/elif/else - compõe mais de dois desvios, mais de uma expressão verdadeira (if e elif), caso for falso, retorna o else
opcao = int(input("informe a opção: 1 Sacar \n2 extrato: "))
if opcao == 1:
    valor = float(input("informe o valor do saque: "))
elif opcao == 2:
    print("extrato")
else:
    print("opção inválida")





if opcao == 1:
    print("saque realizado com sucesso")
elif opcao == 2:
    print("extrato")
else:
    sys.exit("opção inválida")



# if aninhado
# if ternário