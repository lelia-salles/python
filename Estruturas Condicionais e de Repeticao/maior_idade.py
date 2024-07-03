MAIOR_IDADE = 18 # letra maúscula indica constante

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH")
else:
    print("Você é menor de idade")

print("Fim do programa")