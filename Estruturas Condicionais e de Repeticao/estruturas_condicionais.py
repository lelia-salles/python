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


# if aninhado
# if ternário