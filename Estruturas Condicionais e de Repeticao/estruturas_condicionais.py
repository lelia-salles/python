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
    SystemExit("opção inválida")

 

# if aninhado
saldo1 = 2000.0
saque1 = float(input("informe valo do saque"))
conta_bloqueada = False  # Define a variable to track if the account is blocked

if not conta_bloqueada:  # Check if the account is not blocked
    if saldo1 >= saque1:  # Check if the balance is sufficient for the withdrawal
        print("saque realizado com sucesso")
    elif saldo1 < saque1:
        print("saldo insuficiente")
else:
    print("conta bloqueada")


# if ternário
saldo = 2000.0
saque = float(input("informe valo do saque"))

print("saque realizado com sucesso") if saldo >= saque else print("saldo insuficiente")

# if ternário com variável
saldo = 2000.0
saque = float(input("informe valo do saque"))

mensagem = "saque realizado com sucesso" if saldo >= saque else "saldo insuficiente"
print(mensagem)

# if ternário com variável e função
saldo = 2000.0
saque = float(input("informe valo do saque"))

def sacar(saldo, saque):
    return "saque realizado com sucesso" if saldo >= saque else "saldo insuficiente"

mensagem = sacar(saldo, saque)
print(mensagem)

# if ternário com variável e função e return
saldo = 2000.0
saque = float(input("informe valo do saque"))

def sacar(saldo, saque):
    return "saque realizado com sucesso" if saldo >= saque else "saldo insuficiente"

print(sacar(saldo, saque))

# if ternário com variável e função e return e print
saldo = 2000.0
saque = float(input("informe valo do saque"))

def sacar(saldo, saque):
    return "saque realizado com sucesso" if saldo >= saque else "saldo insuficiente"

print(sacar(saldo, saque))

# if ternário com variável e função e return e print e if
saldo = 2000.0
saque = float(input("informe valo do saque"))

def sacar(saldo, saque):
    return "saque realizado com sucesso" if saldo >= saque else "saldo insuficiente"

if sacar(saldo, saque) == "saque realizado com sucesso":
    print("saque realizado com sucesso")
else:
    print("saldo insuficiente")

# if ternário com variável e função e return e print e if e else

