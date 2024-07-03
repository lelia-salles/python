MAIOR_IDADE = 18 # letra maúscula indica constante
IDADE_ESPECIAL = 12


idade = int(input("Digite sua idade: "))


if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH")

else:
    print("Você é menor de idade")

print("Fim do programa")


if idade >= MAIOR_IDADE:
    print("você pode tirar a CNH")

elif idade >= IDADE_ESPECIAL  :
    print("Você pode fazer as teóricas")

else:
    print("Você não pode tirar a CNH")
    print("Você não pode fazer as teóricas")


print("Fim do programa")

